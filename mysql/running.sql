USE bancodeteste;

CREATE TABLE Course (
    course_id INT NOT NULL AUTO_INCREMENT,
    name VARCHAR(50),
    type VARCHAR(20),
    PRIMARY KEY (course_id)
);

CREATE TABLE Subject (
    subject_id INT NOT NULL AUTO_INCREMENT,
    name VARCHAR(50),
    PRIMARY KEY (subject_id)
);

CREATE TABLE Vinculations (
    course_id INT NOT NULL,
    subject_id INT NOT NULL,
    FOREIGN KEY (course_id)
        REFERENCES Course(course_id)
        ON DELETE CASCADE,
    FOREIGN KEY (subject_id)
        REFERENCES Subject(subject_id)
        ON DELETE CASCADE   
);