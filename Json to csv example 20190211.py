# -*- coding: utf-8 -*-
"""
Created on Mon Feb 11 15:46:17 2019

@author: millerk2
"""

import sys
import pprint
import xlsxwriter
import csv
import json

class FileManagement:
    def __init__(self):
        self.json_file_name = "C:\\Users\\millerk2\\Documents\\Python Scripts\\Incidents JSON.json"
        self.json_file_name_dump = "C:\\Users\\millerk2\\Documents\\Python Scripts\\Incidents JSON4.json"
        self.excel_file_name = "C:\\Users\\millerk2\\Documents\\Python Scripts\\Incidents JSON2.csv"
        self.objid = []
        self.Project_Name = []
        self.Incident_ID = []
        self.Date_ = []
        self.Reg_Reqmnt = []
        self.Reg_Reqmnt_RefNo = []
        self.Compliance_Level = []
        self.Contractor_ = []
        self.Status_ = []
#        self.array_sum = []
    def read_text_file(self):
        try:
            with open(self.json_file_name, 'r') as data_file:
                data_1st = json.load(data_file)

#                *** Try getting it into the ["DATA"][0] mode before dumping it back.

                json.dump(data_1st, self.json_file_name_dump, sort_keys = False, indent=4)
                self.print("Loaded JSON data")
                data = json.load(self.json_file_name_dump)
                self.print(data)
                rows = [line for line in data]
                pprint.pprint(rows[0])
#                pprint.pprint(data)
                for each_axis in data["DATA"]:
                    print(["DATA"])
                    objid = int(each_axis["OBJID"])
##                    objid = each_axis["OBJID"]                    
##                    Project_Name = int(each_axis["PROJECT_NAME"])
                    Project_Name = int(each_axis["PROJECT_NAME"])
#                    print(objid)
#                    Incident_ID = int(each_axis["INCIDENT_ID"])
#                    Date_ = int(each_axis["DATE_"])
#                    Reg_Reqmnt = int(each_axis["REGULATORY_REQUIREMENT"])
#                    Reg_Reqmnt_RefNo = int(each_axis["REGULATORY_REQUIREMENT_REFERENCE_NO"])
#                    Compliance_Level = int(each_axis["COMPLIANCE_LEVEL"])
#                    Contractor_ = int(each_axis["CONTRACTOR_"])
#                    Status_ = int(each_axis["STATUS_"])
                    self.array_objid.append(self.objid)
                    self.array_Project_Name.append(self.Project_Name)
                    print(self.objid)
#                    self.array_Incident_ID.append(Incident_ID)
#                    self.array_Date_.append(Date_)
#                    self.array_Reg_Reqmnt.append(Reg_Reqmnt)
#                    self.array_Reg_Reqmnt_RefNo.append(Reg_Reqmnt_RefNo)
#                    self.array_Compliance_Level.append(Compliance_Level)
#                    self.array_Contractor_.append(Contractor_)
#                    self.array_Status_.append(Status_)               
##                    self.array_sum.append(x + y)
                    pprint.pprint("OBJID = {0}".format(objid))
                    pprint.pprint("PROJECT_NAME = {0}".format(Project_Name))
#                    print(["PROJECT NAME"][0])
#                    pprint.pprint("INCIDENT_ID = {0}".format(Incident_ID))
#                    pprint.pprint("DATE_ = {0}".format(Date_))
#                    pprint.pprint("REGULATORY_REQUIREMENT = {0}".format(Reg_Reqmnt))
#                    pprint.pprint("REGULATORY_REQUIREMENT_REFERENCE_NO = {0}".format(Reg_Reqmnt_RefNo))
#                    pprint.pprint("COMPLIANCE_LEVEL = {0}".format(Compliance_Level))
#                    pprint.pprint("CONTRACTOR_ = {0}".format(Contractor_))
#                    pprint.pprint("STATUS_ = {0}".format(Status_))
        except:
            print("It did nothing")
            print("Unexpected error : ", sys.exc_info()[0])
            raise

    def save_to_xlsx(self):
        self.pprint.pprint("Started save to step")
#        writer = csv.writer(self.excel_file_name)
        workbook = xlsxwriter.Workbook(self.excel_file_name)
        worksheet = workbook.add_worksheet()
        for index, value in enumerate(self.data["DATA"]):
#            writer.writerow(index, 0, self.array_objid[index]) #column 0
#            writer.writerow(index, 1, self.array_Project_Name[index])
            print([index])
#            writer.writerow(index, 2, self.array_Incident_ID[index])
#            writer.writerow(index, 3, self.array_Date_[index])
#            writer.writerow(index, 4, self.array_Reg_Reqmnt[index])
#            writer.writerow(index, 5, self.array_Reg_Reqmnt_RefNo[index])
#            writer.writerow(index, 6, self.array_Compliance_Level[index])
#            writer.writerow(index, 7, self.array_Contractor_[index])
#            writer.writerow(index, 8, self.array_Status_[index])
            print(index)
#
            worksheet.write(index, 0, self.array_objid[index]) #column 0
            worksheet.write(index, 1, self.array_Project_Name[index])
##            worksheet.write(index, 2, self.array_Incident_ID[index])
##            worksheet.write(index, 3, self.array_Date_[index])
##            worksheet.write(index, 4, self.array_Reg_Reqmnt[index])
##            worksheet.write(index, 5, self.array_Reg_Reqmnt_RefNo[index])
##            worksheet.write(index, 6, self.array_Compliance_Level[index])
##            worksheet.write(index, 7, self.array_Contractor_[index])
##            worksheet.write(index, 8, self.array_Status_[index])
        worksheet.close()
        
print("Made it to the end")
if __name__ == '__main__':
    print("File name must equal __main__")
    file_management = FileManagement()
    file_management.read_text_file()
    file_management.save_to_xlsx()
else:
    print("File name did not equal __main__")