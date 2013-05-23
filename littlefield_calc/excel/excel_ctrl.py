import csv


class DataController():
    def _load_array_of_content(self, filename):
        content = []
        with open(filename, 'r') as station_machine:
            c = csv.reader(station_machine, delimiter='\t', skipinitialspace=True)
            for line in c:
                content.append(line)
        return content

    def _cal_average_value(self, contents, days_ago):
        content = contents[1:]
        amount = 0
        value_summary = 0
        for data in reversed(content):
            value = float(data[1])
            value_summary += value
            amount += 1
            if amount == days_ago:
                break
        return value_summary/amount, amount

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

    empty_queue_dates = []
    #def _cal_maximum_capaity_of_each_station(self):
    for s1 in reversed(station_1_queue_contents):
        if s1[1] == '0':
            for s2 in station_2_queue_contents:
                if s2[0] == s1[0]:
                    if s2[1] == '0':
                        for s3 in station_3_queue_contents:
                            if s3[0] == s2[0]:
                                if s3[1] == '0':
                                    empty_queue_dates.append(s3[0])

    def _calculate_maximum_capacity(self, station_utilization_contents, empty_queue_dates, complete_job_contents):
        max_capacities = []
        for empty_queue_date in empty_queue_dates:
            for station in station_utilization_contents:
                if station[0] == empty_queue_date:
                    for completed_job in complete_job_contents:
                        if completed_job[0] == empty_queue_date:
                            kit_amount = int(completed_job[1]) * 60
                            try:
                                maximum_capacity = kit_amount/float(station[1])
                            except ZeroDivisionError:
                                maximum_capacity = 'no work'
                            max_capacities.append([empty_queue_date, maximum_capacity])
        return max_capacities

    empty_queue_capa_1 = _calculate_maximum_capacity([], station_1_utilization_contents, empty_queue_dates, complete_job_contents)
    empty_queue_capa_2 = _calculate_maximum_capacity([], station_2_utilization_contents, empty_queue_dates, complete_job_contents)
    empty_queue_capa_3 = _calculate_maximum_capacity([], station_3_utilization_contents, empty_queue_dates, complete_job_contents)

    with open('d:/test/summary.xls', 'w') as little_field_summary:
        # merge content to summary.xls
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

        for i in range(5):
            i += 1
            avg_util_1, working_1_day = _cal_average_value([], station_1_utilization_contents, i * 10)
            little_field_summary.write('AVG S1 is %s for last %s days' % (avg_util_1, working_1_day))
            little_field_summary.write('\n')
            avg_util_2, working_2_day = _cal_average_value([], station_2_utilization_contents, i * 10)
            little_field_summary.write('AVG S2 is %s for last %s days' % (avg_util_2, working_2_day))
            little_field_summary.write('\n')
            avg_util_3, working_3_day = _cal_average_value([], station_3_utilization_contents, i * 10)
            little_field_summary.write('AVG S3 is %s for last %s days' % (avg_util_3, working_3_day))
            little_field_summary.write('\n')
            little_field_summary.write('\n')

        for i in range(5):
            i += 1
            avg_value_1, working_1_day = _cal_average_value([], lead_time_contents, i * 10)
            little_field_summary.write('AVG lead-time is %s for last %s days' % (avg_value_1, working_1_day))
            little_field_summary.write('\n')
            little_field_summary.write('\n')

        little_field_summary.write('date\tS1\tS2\tS3')
        little_field_summary.write('\n')
        for index, date in enumerate(empty_queue_dates):
            little_field_summary.write(date)
            little_field_summary.write('\t')
            little_field_summary.write(str(empty_queue_capa_1[index][1]))
            little_field_summary.write('\t')
            little_field_summary.write(str(empty_queue_capa_2[index][1]))
            little_field_summary.write('\t')
            little_field_summary.write(str(empty_queue_capa_3[index][1]))
            little_field_summary.write('\n')
