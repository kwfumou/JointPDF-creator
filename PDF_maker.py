class generater_status:

    task_flag = False
    PDF_name = 'none'
    band_width = 0.
    num_sample = 0
    time_stamp = 0.1
    generation_time = 0.
    response_time = 0.
    PDF_list = {
        'bimodal',
        'laplace',
        'log',
        'gamma'
    }

    def __init__(self):
        print('genarate PDF_maker')

    def get_status(self):
        # print('get status')
        # print('PDF name:',self.PDF_name)
        # get_pdf = self.PDF_name
        # self.PDF_name = 'none'
        # return get_pdf

        if self.task_flag == True:
            print('PDF name:',self.PDF_name)

            # send_par
            get_pdf = self.PDF_name
            get_width = self.band_width
            get_nSample = self.num_sample
            get_timeStamp = self.time_stamp
            get_genTime = self.generation_time
            get_resTime = self.response_time

            # clear
            self.PDF_name = 'none'
            self.band_width = 0.
            self.num_sample = 0
            self.time_stamp = 0.1
            self.task_flag = False
            return [True,get_pdf,get_width,get_nSample,get_timeStamp,get_genTime,get_resTime]
        else:
            return [self.task_flag,'none_test']
        
    def change_status(self,pdf_name,band_width_,num_sample_,time_stamp_,generation_time_,response_time_):
        if pdf_name in self.PDF_list:
            self.PDF_name = pdf_name
            self.task_flag = True
            self.band_width = band_width_
            self.num_sample = num_sample_
            self.time_stamp = time_stamp_
            self.generation_time = generation_time_
            self.response_time = response_time_