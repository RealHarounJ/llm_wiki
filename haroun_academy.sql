/* 
   Haroun Academy (Global E-Learning Platform) - SQL DDL Script 
   Academic Level: University (Conceptual -> Logical -> Physical)
*/

-- 1. Base Entity: USER
CREATE TABLE USER_ACCOUNT (
    user_id INT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL
);

-- 2. Subclass: INSTRUCTOR
CREATE TABLE INSTRUCTOR (
    user_id INT PRIMARY KEY,
    bio TEXT,
    hourly_rate DECIMAL(10, 2),
    FOREIGN KEY (user_id) REFERENCES USER_ACCOUNT(user_id) ON DELETE CASCADE
);

-- 3. Subclass: STUDENT
CREATE TABLE STUDENT (
    user_id INT PRIMARY KEY,
    registration_date DATE NOT NULL,
    FOREIGN KEY (user_id) REFERENCES USER_ACCOUNT(user_id) ON DELETE CASCADE
);

-- 4. Multi-valued Attribute Mapping: STUDENT_INTERESTS
CREATE TABLE STUDENT_INTERESTS (
    user_id INT,
    interest VARCHAR(50),
    PRIMARY KEY (user_id, interest),
    FOREIGN KEY (user_id) REFERENCES STUDENT(user_id) ON DELETE CASCADE
);

-- 5. Main Entity: COURSE
CREATE TABLE COURSE (
    course_code VARCHAR(20) PRIMARY KEY,
    title VARCHAR(200) NOT NULL,
    price DECIMAL(10, 2) NOT NULL,
    instructor_id INT NOT NULL,
    FOREIGN KEY (instructor_id) REFERENCES INSTRUCTOR(user_id) ON DELETE CASCADE
);

-- 6. Recursive M:N Relationship: PREREQUISITE
CREATE TABLE PREREQUISITE (
    main_course_code VARCHAR(20),
    prereq_course_code VARCHAR(20),
    PRIMARY KEY (main_course_code, prereq_course_code),
    FOREIGN KEY (main_course_code) REFERENCES COURSE(course_code) ON DELETE CASCADE,
    FOREIGN KEY (prereq_course_code) REFERENCES COURSE(course_code) ON DELETE CASCADE
);

-- 7. Weak Entity Mapping: LESSON
CREATE TABLE LESSON (
    course_code VARCHAR(20),
    lesson_number INT,
    title VARCHAR(150) NOT NULL,
    duration_minutes INT,
    PRIMARY KEY (course_code, lesson_number),
    FOREIGN KEY (course_code) REFERENCES COURSE(course_code) ON DELETE CASCADE
);
