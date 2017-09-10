import sql_connection


class sql_handler:
    string_to_exe = ""
    @sql_connection.connection_handler
    def quarie(cursor,self):
        cursor.execute(self.string_to_exe)
        result = cursor.fetchall()
        return result

mentors_schools = sql_handler()
mentors_schools.string_to_exe = """SELECT schools.name as school_name,schools.country,first_name,last_name
                FROM mentors
                JOIN schools
                ON mentors.city = schools.city
                order by mentors.id"""


all_school = sql_handler()
all_school.string_to_exe = """SELECT schools.name as school_name,schools.country, first_name,last_name
                FROM mentors
                right JOIN schools
                ON mentors.city = schools.city
                order by mentors.id"""


mentors_by_country = sql_handler()
mentors_by_country.string_to_exe = """SELECT COUNT(schools.country), schools.country
                FROM mentors
                JOIN schools
                ON mentors.city = schools.city
                group by schools.country
                order by schools.country"""


contacts = sql_handler()
contacts.string_to_exe = """SELECT schools.name, first_name, last_name
                FROM mentors
                JOIN schools
                ON mentors.id = schools.contact_person
                order by schools.name"""


applicants = sql_handler()
applicants.string_to_exe = """SELECT first_name, application_code, applicants_mentors.creation_date
                FROM applicants
                JOIN applicants_mentors
                ON applicants.id = applicants_mentors.applicant_id
                where applicants_mentors.creation_date > '2016-01-01'"""


applicants_and_mentors = sql_handler()
applicants_and_mentors.string_to_exe = """SELECT applicants.first_name as applicants_first_name, applicants.application_code, mentors.nick_name as mentors_nick_name
                FROM applicants
                left JOIN applicants_mentors
                on applicants.id = applicants_mentors.applicant_id
                left JOIN mentors
                on mentors.id = applicants_mentors.mentor_id"""
