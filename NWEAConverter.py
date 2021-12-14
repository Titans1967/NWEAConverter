#NWEA Map Rostering Automation
# Title: NWEA.py
# Purpose: To automate NWEA and edit rf.csv with the correct edits automatically
# Author: cpashcall & cwilliams & cmiller
# Date: 2021-10-29
# Changes:
# Who/When/What


#import support modules
import csv  
import os
import sys
import time
import timeit
#import fileinput

#variables
vstart = time.time()
fileDateTime = time.strftime("%Y%m%d-%H%M%S")
fileDateTime = time.strftime("%Y%m%d-%H%M%S")
vTime = time.strftime("%H%M%S")
vDate = time.strftime("%m%d%Y")

#What is the current working directory, for testing
v_cwd = os.getcwd()
print ('Current Dir '+ v_cwd)
#os.chdir('C:\\Users\\cwilliams2\\Documents\\Python\\Scripts')
#os.chdir('C:\\Users\\cwilliams2\\OneDrive - Trinity Basin\\Documents\\Python\\Scripts')
#v_cwd = os.getcwd()
#print ('New Current Dir '+ v_cwd)

#File Definitions
#Add code to move file from Downloads directory into Python directory for processing
#Currenly import files reside in the C:\Users\cwilliams2\OneDrive - Trinity Basin\Documents\Python directory
#i_ = input file
#o_ = output file
#l_log_file = open("NWEAMap_rostering_file_prep.log",mode="w")
#l_log_comm = "NWEA Map Rostering Automation.py executed on " + fileDateTime
#print(l_log_comm, file=l_log_file)
#ui_file = input("NWEA Map input file name, default 'rf.csv': ")
#if ui_file != '':
    #i_File = ui_file
#else:
    #i_File = 'C:\\Users\cwilliams2\\OneDrive - Trinity Basin\\Documents\\Python\\Scripts\\rf.csv'
    #i_File = "rf.csv"
#i_File = 'rf.csv'
i_File = 'C:\\Users\cwilliams2\\OneDrive - Trinity Basin\\Documents\\Python\\Scripts\\rf.csv'
#l_log_comm = "Input file name is "+ i_File
#print (l_log_comm)
#print (l_log_comm, file=l_log_file)
#Currently export files reside in the C:\Users\cwilliams2\OneDrive - Trinity Basin\Documents\Python\Scripts directory
#print("Output dir: C:\Users\cwilliams2\OneDrive - Trinity Basin\Documents\Python\Scripts")

o_File = "C:\\Users\cwilliams2\\OneDrive - Trinity Basin\\Documents\\Python\\Scripts\\rf" + fileDateTime + ".csv"

#set up outputfile to collect transformed data
ho_File = open(o_File, mode='w', newline='')
#fieldnames = ['Student ID', 'First Name', 'Middle Name', 'Last Name', 'Gender', 'Birth Date', 'Student Grade', 'School ID', 'School ID', 'Hisp/Lat Eth', 'American Indian/Alaskan Native', 'Black/African American', 'Hawaiian/Pacific Islander', 'Asian', 'White', 'Birth City', 'Home Language', 'Language Code', 'Street Number', 'Street Name', 'F1/G1 Phone Number', 'F1/G1 First Name', 'F1/G1 Last Name', 'F1/G1 Relation', 'F1/G1 Email', 'F2/G2 Phone Number', 'F2/G2 First Name', 'F2/G2 Last Name', 'F2/G2 Relation', 'F2/G2 Email', 'SSN or SIN', 'Address City', 'Address State', 'Address Zip', 'Submission Date']
#SMWriter = csv.DictWriter(SchoolMintFileFixed, fieldnames=fieldnames)
#SMWriter.writeheader()

fieldnames = ['School State Code', 'School Name', 'Previous Instructor ID', 'Instructor ID', 'Instructor State ID', 'Instructor Last Name', 'Instructor First Name', 'Instructor Middle Initial', 'User Name', 'Email Address', 'Class Name', 'Subject', 'Previous Student ID', 'Student ID', 'Student State ID', 'ClassLink ID', 'OneRoster ID', 'Student Last Name', 'Student First Name', 'Student Middle Initial', 'Student Date Of Birth', 'Student Gender', 'Student Grade', 'Student Ethnic Group Name', 'Student User Name', 'Student Email']
SMWriter = csv.DictWriter(ho_File, fieldnames=fieldnames)
SMWriter.writeheader()

# the csv file from SchoolMint is UTF-8 encoded and appears to lead with BOM, handled by encoding='utf-8-sig'
with open(i_File, mode='r', encoding='utf-8-sig') as csv_file: 

    csv_reader = csv.DictReader(csv_file)

    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
        line_count += 1
        #print('Line Count: '+str(line_count))
        
        #print(f'{row["Student ID"]} is {row["First Name"]} {row["Middle Name"]} {row["Last Name"]} and was born at {row["F1 Street Number"]}.')
        #School State Code, School Name, Previous Instructor ID, Instructor ID, Instructor State ID, Instructor Last Name, Instructor First Name, Instructor Middle Initial, User Name, Email Address, Class Name, Subject, Previous Student ID, Student ID, Student State ID, ClassLink ID, OneRoster ID, Student Last Name, Student First Name, Student Middle Initial, Student Date Of Birth, Student Gender, Student Grade, Student Ethnic Group Name, Student User Name, Student Email
        #print (f'{row["School State Code"]}, {row["School Name"]}, {row["Previous Instructor ID"]},{row["Instructor ID"]}, {row["Instructor State ID"]}, {row["Instructor Last Name"]}, {row["Instructor First Name"]},{row["Instructor Middle Initial"]}, {row["User Name"]},{row["Email Address"]},{row["Class Name"]}, {row["Subject"]},{row["Previous Student ID"]},{row["Student ID"]},{row["Student State ID"]},{row["ClassLink ID"]},{row["OneRoster ID"]},{row["Student Last Name"]},{row["Student First Name"]},{row["Student Middle Initial"]},{row["Student Date Of Birth"]},{row["Student Gender"]},{row["Student Grade"]},{row["Student Ethnic Group Name"]},{row["Student User Name"]},{row["Student Email"]}')
        l_newSEGN = str({row["Student Ethnic Group Name"]})
        if {row["Student Ethnic Group Name"]} == "American Indian or Alaskan Native":
            l_newSEGN = "American Indian or Alaska Native"
            #print('Changed ethnicity.')
        l_newGrade = str({row["Student Grade"]})
        if {row["Student Grade"]} == "IT":
            l_newGrade = "PK"
        #len_ILN = len({row["Instructor Last Name"]})
        #print('Instructor Last Name: ' +str({row["Instructor Last Name"]}))
        #print (len_ILN)

        #clean up data output fields no longer in the dictionary
        l_newSEGN = l_newSEGN.replace("'","")
        l_newSEGN = l_newSEGN.replace("{","")
        l_newSEGN = l_newSEGN.replace("}","")

        l_newGrade = l_newGrade.replace("'","")
        l_newGrade = l_newGrade.replace("{","")
        l_newGrade = l_newGrade.replace("}","")
        
        # If the class does not have an instructor, this will cause an error on import to the remote system, so do not write that record
        if row["Instructor Last Name"] !='':
            SMWriter.writerow({'School State Code': row["School State Code"],'School Name': row["School Name"], 'Previous Instructor ID': row["Previous Instructor ID"],'Instructor ID': row["Instructor ID"], 'Instructor State ID': row["Instructor State ID"], 'Instructor Last Name': row["Instructor Last Name"], 'Instructor First Name': row["Instructor First Name"], 'Instructor Middle Initial': row["Instructor Middle Initial"], 'User Name': row["User Name"],'Email Address': row["Email Address"],'Class Name': row["Class Name"], 'Subject': row["Subject"],'Previous Student ID': row["Previous Student ID"],'Student ID': row["Student ID"],'Student State ID': row["Student State ID"],'ClassLink ID': row["ClassLink ID"],'OneRoster ID': row["OneRoster ID"],'Student Last Name': row["Student Last Name"],'Student First Name': row["Student First Name"],'Student Middle Initial': row["Student Middle Initial"],'Student Date Of Birth': row["Student Date Of Birth"],'Student Gender': row["Student Gender"],'Student Grade': l_newGrade,'Student Ethnic Group Name': l_newSEGN,'Student User Name': row["Student User Name"],'Student Email': row["Student Email"]})

#l_log_comm="Processed " + str(line_count) + " lines from RosterServer export, "+ i_File +", into transform file, "+ o_File +" for NWEA import."
#print(l_log_comm)
#print (l_log_comm, file=l_log_file)

#Close files if needed
ho_File.close()
#l_log_file.close()
