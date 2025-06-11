from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import NewGeneratorData
from .serializers import NewGeneratorDataSerializer
from django.http import HttpResponse
from django.utils import timezone
import csv
 

@api_view(['POST'])
def receive_generator_data(request):
    try:
        print("Received data:", request.data)  # Debug log
        
        # Define the field mappings for each array
        array_mappings = {
            "array_[i]": [
                ('control_switch_position', 1, {0: 'Off', 1: 'Auto', 2: 'Manual'}),
                ('genset_state', 1, {
                    0: 'Off', 1: 'Stop', 2: 'Preheat', 3: 'Precrank', 4: 'Crank', 5: 'Starter Disconnect',
                    6: 'PreRamp', 7: 'Ramp', 8: 'Running', 9: 'Fault Shutdown', 10: 'Prerun Setup',
                    11: 'Runtime Setup', 12: 'Factory Test', 13: 'Waiting For Powerdown'
                }),
                ('current_fault', 1, None),
                ('current_fault_severity', 1, {0: 'None', 1: 'Warning', 2: 'Shutdown'})
            ],
            "array_[iii]": [
                ('genset_l1_n_rms_voltage', 0.1, None),
                ('genset_l2_n_rms_voltage', 0.1, None),
                ('genset_l3_n_rms_voltage', 0.1, None)
            ],
            "array_[iv]": [
                ('genset_l1_l2_rms_voltage', 0.1, None),
                ('genset_l2_l3_rms_voltage', 0.1, None),
                ('genset_l3_l1_rms_voltage', 0.1, None)
            ],
            "array_[v]": [
                ('genset_l1_rms_current', 0.1, None),
                ('genset_l2_rms_current', 0.1, None),
                ('genset_l3_rms_current', 0.1, None)
            ],
            "array_[vi]": [
                ('genset_l1_kw', 0.1, None),
                ('genset_l2_kw', 0.1, None),
                ('genset_l3_kw', 0.1, None),
                ('genset_total_kw', 0.1, None),
                ('genset_l1_kvar', 0.1, None),
                ('genset_l2_kvar', 0.1, None),
                ('genset_l3_kvar', 0.1, None),
                ('genset_total_kvar', 0.1, None)
            ],
            "array_[vii]": [
                ('genset_l1_kva', 0.1, None),
                ('genset_l2_kva', 0.1, None),
                ('genset_l3_kva', 0.1, None),
                ('genset_total_kva', 0.1, None),
                ('genset_frequency', 0.01, None)

                 ],
            "array_[viii]": [
                ('battery_voltage', 0.1, None),
                ('oil_pressure', 0.1, None)
            ],
            "array_[ix]": [
               ('coolant_temperature', 0.1, None)
            ],
            "array_[x]": [
                ('average_engine_speed', 1, None),
                ('start_attempts', 1, None)
            ],
            "array_[xi]": [
                ('Utility L1-N RMS Voltage', 1, None),
                ('Utility L2-N RMS Voltage', 1, None),
                ('Utility L3-N RMS Voltage', 1, None)
            ],
            "array_[xii]": [
                ('Utility L1-L2 RMS Voltage', 1, None),
                ('Utility L2-L3 RMS Voltage', 1, None),
                ('Utility L3-L1 RMS Voltage', 1, None)
            ],
            "array_[xiv]": [
                ('charging_alternator_voltage', 0.1, None)
            ],
            "array_[xv]": [
                ('modbus_remote_start', 1, {0: 'Inactive', 1: 'Active'}),
                ('modbus_fault_reset', 1, {0: 'Inactive', 1: 'Active'}),
                ('network_shutdown_modbus_command', 1, {0: 'Inactive', 1: 'Active'}),
                
            ]
        }

        # Get the data directly from request.data
        all_data = request.data
        print("Received data:", all_data)  # Debug log
        
        if not isinstance(all_data, dict):
            return Response({'error': 'Data must be a dictionary of register arrays.'}, status=status.HTTP_400_BAD_REQUEST)

        saved_records = []
        mapped_data = {}

        # Process each array in the data
        for array_name, data_array in all_data.items():
            print(f"Processing array {array_name}: {data_array}")  # Debug log
            
            if array_name not in array_mappings:
                print(f"Skipping unknown array: {array_name}")
                continue

            if not isinstance(data_array, list):
                print(f"Skipping {array_name}: not a list")
                continue

            # Get the field mappings for this array
            fields = array_mappings[array_name]
            
            # Map the values to their corresponding fields
            for idx, (field, multiplier, enum_dict) in enumerate(fields):
                if idx >= len(data_array):
                    print(f"Warning: {array_name} array too short, skipping remaining fields")
                    break
                    
                val = data_array[idx]
                print(f"Processing value {val} for field {field}")  # Debug log
                
                try:
                    val = float(val) * multiplier
                except Exception as e:
                    print(f"Error converting value {val} to float: {e}")  # Debug log
                    pass
                    
                if enum_dict is not None:
                    try:
                        val = enum_dict.get(int(data_array[idx]), val)
                    except Exception as e:
                        print(f"Error mapping enum value {val}: {e}")  # Debug log
                        pass
                        
                mapped_data[field] = val
                print(f"Mapped {field} to {val}")  # Debug log

        print("Final mapped data:", mapped_data)  # Debug log

        try:
            # Create and save the generator data
            generator_data = NewGeneratorData(**mapped_data)
            generator_data.save()
            serializer = NewGeneratorDataSerializer(generator_data)
            saved_records.append(serializer.data)
            print(f"Successfully saved data")
        except Exception as save_error:
            print(f"Failed to save data: {save_error}")
            return Response({'error': str(save_error)}, status=status.HTTP_400_BAD_REQUEST)

        return Response({'saved': saved_records}, status=status.HTTP_201_CREATED)

    except Exception as e:
        print(f"Error in receive_generator_data: {str(e)}")
        return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def generator_data_csv(request):
    days = int(request.GET.get('days', 1))
    days = min(max(days, 1), 30)  # Clamp between 1 and 30
    since = timezone.now() - timezone.timedelta(days=days)
    queryset = NewGeneratorData.objects.filter(timestamp__gte=since).order_by('-timestamp')
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = f'attachment; filename="generator_data_last_{days}_days.csv"'
    writer = csv.writer(response)
    fields = [f.name for f in NewGeneratorData._meta.fields]
    writer.writerow(fields)
    for obj in queryset:
        writer.writerow([getattr(obj, f) for f in fields])
    return response

@api_view(['GET'])
def get_latest_generator_data(request):
    try:
        latest_data = NewGeneratorData.objects.order_by('-timestamp').first()
        if latest_data:
            serializer = NewGeneratorDataSerializer(latest_data)
            return Response(serializer.data)
        return Response({'error': 'No data available'}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST) 