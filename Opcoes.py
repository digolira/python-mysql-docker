
from enum import IntEnum


#tive q usar IntEnum
class MenuPrincipal (IntEnum):
    CHECK_COURSES_DETAILS = 1
    CHECK_SUBJECTS_DETAILS = 2
    CREATE_COURSE = 3
    CREATE_SUBJECT = 4
    VINCULATE_SUBJECT = 5
    LEAVE = 6
    
class TipoGraduacao(IntEnum):
    GRADUACAO = 1
    MESTRADO = 2
    DOUTORADO = 3