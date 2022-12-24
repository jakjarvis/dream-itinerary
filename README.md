# dream-itinerary

Application to create exciting visual itinerary ideas that can be shared with friends and family, to garner their interest and see if they want to come.

Link to the [Initial Requirements/Workshop](https://docs.google.com/document/d/1Vfa9CjJ6HbZ-uWQzmz2-R_gtZE49-2XjGHBVe1OBcOE/edit)
Link to the [Discovery](https://docs.google.com/presentation/d/1A52rHUqQ7119ffN4SlNmoBytCPrvhJFZOkBNWW9_KQs/edit#slide=id.g18ba4daa95f_1_6)

## Notes for running in Docker

The full application has been dockerized, including the react frontend, django backend and a mysql database. To enable this, the developer needs to go into the settings.py file in the django add and under DATABASES, comment out the local sqlite3 database code and comment in the mysql database code.
