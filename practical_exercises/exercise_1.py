'''
This file is my resolution of the following exercise statement:
    Print the following data:
        a. Difference between the actual course (1.5h) and...
            - The quickest of the other courses (2.5h) 
            - The slowest of the other courses (7h)
            - The average of the other courses (4h)  
        b. Percentage% of useless audiovisual content that is 
        reduced in...
            - The average of the courses
            - The actual course
            - Data: total_audiovisual_this_course = 3.5h 
            total_audiovisual_average_courses = 5h
        c. Watching 10h of this course how many hours seen are 
        equivalent in other courser? And viceversa? 
'''

# A 

ACTUAL_COURSE_H = 1.5
QUICKEST_COURSE_H = 2.5
SLOWEST_COURSE_H = 7
AVERAGE_COURSE_H = 4

print('The difference of this course with the... \n- quickest is of: {0}h \n- slowest is of: {1}h \n- average is of: {2}h'.format(QUICKEST_COURSE_H - ACTUAL_COURSE_H,
                                                                                                                           SLOWEST_COURSE_H - ACTUAL_COURSE_H,
                                                                                                                           AVERAGE_COURSE_H - ACTUAL_COURSE_H))

# B

TOTAL_AUDIOVISUAL_THIS_COURSE = 3.5
TOTAL_AUDIOVISUAL_AVERAGE_COURSES = 5

percentatge_useless_content_this_course = round((TOTAL_AUDIOVISUAL_THIS_COURSE - ACTUAL_COURSE_H) / TOTAL_AUDIOVISUAL_THIS_COURSE * 100, 2) # the value needs to be multiplied by 100 in order to be a percentatge
percentatge_useless_content_average_courses = round((TOTAL_AUDIOVISUAL_AVERAGE_COURSES - AVERAGE_COURSE_H) / TOTAL_AUDIOVISUAL_AVERAGE_COURSES * 100, 2) 


print('The percentatge of useless audiovisual content is:\n - {}% in this course\n - {}% in the average course'.format(percentatge_useless_content_this_course, percentatge_useless_content_average_courses))


# C

HOURS_EQUIVALENCE = 10

print(f"Watching 10h of Dalton's course, equals to {round(HOURS_EQUIVALENCE * AVERAGE_COURSE_H / ACTUAL_COURSE_H, 2)}h of the average course and watching 10h of the average course, equals to {round(HOURS_EQUIVALENCE * ACTUAL_COURSE_H // AVERAGE_COURSE_H, 2)}h of the Dalton's course")
