import os
import csv

current_directory = os.getcwd()


class DataController():
    def _load_array_of_content(self, filename):
        content = []
        with open(filename, 'r') as station_machine:
            c = csv.reader(station_machine, delimiter='\t', skipinitialspace=True)
            for line in c:
                content.append(line)
        return content

    job_arrival_contents = _load_array_of_content([], 'd:/test/job_arrival.xls')
    job_queue_contents = _load_array_of_content([], 'd:/test/job_q.xls')

    station_1_queue_contents = _load_array_of_content([], 'd:/test/s1q.xls')
    station_1_utilization_contents = _load_array_of_content([], 'd:/test/s1u.xls')
    station_2_queue_contents = _load_array_of_content([], 'd:/test/s2q.xls')
    station_2_utilization_contents = _load_array_of_content([], 'd:/test/s2u.xls')
    station_3_queue_contents = _load_array_of_content([], 'd:/test/s3q.xls')
    station_3_utilization_contents = _load_array_of_content([], 'd:/test/s3u.xls')

    complete_job_contents = _load_array_of_content([], 'd:/test/comp_job.xls')
    lead_time_contents = _load_array_of_content([], 'd:/test/lead_time.xls')
    revenue_contents = _load_array_of_content([], 'd:/test/rev.xls')

    job_arrival_contents[0][1] = 'job arrived'
    job_queue_contents[0][1] = 'job queue'

    station_1_queue_contents[0][1] = 'S1Q'
    station_2_queue_contents[0][1] = 'S2Q'
    station_3_queue_contents[0][1] = 'S3Q'
    station_1_utilization_contents[0][1] = 'S1U'
    station_2_utilization_contents[0][1] = 'S2U'
    station_3_utilization_contents[0][1] = 'S3U'

    complete_job_contents = complete_job_contents[1:] #remove header
    complete_job_contents[0][1] = 'job completed'
    lead_time_contents = lead_time_contents[1:] #remove header
    lead_time_contents[0][1] = 'lead time'
    revenue_contents = revenue_contents[1:] #remove header
    revenue_contents[0][1] = 'revenue'

    with open('d:/test/summary.xls', 'w') as little_field_summary:
        for index in range(len(job_arrival_contents)):
            #assume that the date is all the same
            little_field_summary.write(job_arrival_contents[index][0])  #date
            little_field_summary.write('\t')

            little_field_summary.write(job_arrival_contents[index][1])
            little_field_summary.write('\t')
            little_field_summary.write(job_queue_contents[index][1])
            little_field_summary.write('\t')

            little_field_summary.write(station_1_queue_contents[index][1])
            little_field_summary.write('\t')
            little_field_summary.write(station_1_utilization_contents[index][1])
            little_field_summary.write('\t')

            little_field_summary.write(station_2_queue_contents[index][1])
            little_field_summary.write('\t')
            little_field_summary.write(station_2_utilization_contents[index][1])
            little_field_summary.write('\t')

            little_field_summary.write(station_3_queue_contents[index][1])
            little_field_summary.write('\t')
            little_field_summary.write(station_3_utilization_contents[index][1])
            little_field_summary.write('\t')

            little_field_summary.write(complete_job_contents[index][1])
            little_field_summary.write('\t')

            little_field_summary.write(lead_time_contents[index][1])
            little_field_summary.write('\t')

            little_field_summary.write(revenue_contents[index][1])

            little_field_summary.write('\n')



