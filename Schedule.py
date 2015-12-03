'''

    Each row represents a time slot 10, 12, 2
    Each column represents a room 1305, 1212, 1258
    examChart = [[0, 0, 0],
                 [0, 0, 0],
                 [0, 0, 0]]
'''


class Schedule:
    def __init__(self, courseList):
        self.courseList = courseList
        self.examChart = [[0, 0, 0],
                          [0, 0, 0],
                          [0, 0, 0]]

    def schedule(self):
        self.examChart[0][0] = self.courseList[0]
        room_1305_count = 0
        room_1212_count = 0
        room_1258_count = 0

        exams_not_schedule = []
        schedulecourse = [[self.courseList[0][0:3], self.courseList[0][-6:-3], self.courseList[0][-2:], '1305', '10']]
        room_1305_count += 1

        for element in range(1, len(self.courseList)):
            class_code = self.courseList[element]

            for row in range(len(schedulecourse)):
                if class_code[0:3] == schedulecourse[row][0]:
                    if class_code[-6:-3] == schedulecourse[row][1]:
                        section = schedulecourse[row][2]
                        schedulecourse[row][2] = section + ' ' + class_code[-2:]
                    else:
                        if room_1305_count == 0:
                            schedulecourse.append([class_code[0:3], class_code[-6:-3], class_code[-2:], '1305', '10'])
                            room_1305_count += 1
                            pass
                        elif room_1305_count == 1:
                            schedulecourse.append([class_code[0:3], class_code[-6:-3], class_code[-2:], '1305', '12'])
                            room_1305_count += 1
                            pass
                        elif room_1305_count == 2:
                            schedulecourse.append([class_code[0:3], class_code[-6:-3], class_code[-2:], '1305', '2'])
                            room_1305_count += 1
                            pass
                        elif room_1212_count == 0:
                            schedulecourse.append([class_code[0:3], class_code[-6:-3], class_code[-2:], '1212', '10'])
                            room_1212_count += 1
                            pass
                        elif room_1212_count == 1:
                            schedulecourse.append([class_code[0:3], class_code[-6:-3], class_code[-2:], '1212', '12'])
                            room_1212_count += 1
                            pass
                        elif room_1212_count == 2:
                            schedulecourse.append([class_code[0:3], class_code[-6:-3], class_code[-2:], '1212', '2'])
                            room_1212_count += 1
                            pass
                        elif room_1258_count == 0:
                            schedulecourse.append([class_code[0:3], class_code[-6:-3], class_code[-2:], '1258', '10'])
                            room_1258_count += 1
                            pass
                        elif room_1258_count == 1:
                            schedulecourse.append([class_code[0:3], class_code[-6:-3], class_code[-2:], '1258', '12'])
                            room_1258_count += 1
                            pass
                        elif room_1258_count == 2:
                            schedulecourse.append([class_code[0:3], class_code[-6:-3], class_code[-2:], '1258', '2'])
                            room_1258_count += 1
                            pass
                        else:
                            exams_not_schedule.append(class_code)

                else:
                    if room_1305_count == 0:
                        schedulecourse.append([class_code[0:3], class_code[-6:-3], class_code[-2:], '1305', '10'])
                        room_1305_count += 1
                        pass
                    elif room_1305_count == 1:
                        schedulecourse.append([class_code[0:3], class_code[-6:-3], class_code[-2:], '1305', '12'])
                        room_1305_count += 1
                        pass
                    elif room_1305_count == 2:
                        schedulecourse.append([class_code[0:3], class_code[-6:-3], class_code[-2:], '1305', '2'])
                        room_1305_count += 1
                        pass
                    elif room_1212_count == 0:
                        schedulecourse.append([class_code[0:3], class_code[-6:-3], class_code[-2:], '1212', '10'])
                        room_1212_count += 1
                        pass
                    elif room_1212_count == 1:
                        schedulecourse.append([class_code[0:3], class_code[-6:-3], class_code[-2:], '1212', '12'])
                        room_1212_count += 1
                        pass
                    elif room_1212_count == 2:
                        schedulecourse.append([class_code[0:3], class_code[-6:-3], class_code[-2:], '1212', '2'])
                        room_1212_count += 1
                        pass
                    elif room_1258_count == 0:
                        schedulecourse.append([class_code[0:3], class_code[-6:-3], class_code[-2:], '1258', '10'])
                        room_1258_count += 1
                        pass
                    elif room_1258_count == 1:
                        schedulecourse.append([class_code[0:3], class_code[-6:-3], class_code[-2:], '1258', '12'])
                        room_1258_count += 1
                        pass
                    elif room_1258_count == 2:
                        schedulecourse.append([class_code[0:3], class_code[-6:-3], class_code[-2:], '1258', '2'])
                        room_1258_count += 1
                        pass
                    else:
                        exams_not_schedule.append(class_code)

                        # print(timeSlot10)
                        # print(room1305)
                        # print(self.examChart)
