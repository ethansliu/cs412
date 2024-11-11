from django.db import models

# Create your models here.
class Voter(models.Model):
    last_name = models.TextField()
    first_name = models.TextField()
    street_num = models.IntegerField()
    street_name = models.TextField()
    apt_num = models.TextField()
    zip_code = models.IntegerField()
    birthday = models.TextField()
    registration_date = models.TextField()
    party = models.TextField()
    precinct_num = models.TextField()

    v20_state = models.TextField()
    v21_town = models.TextField()
    v21_primary = models.TextField()
    v22_general = models.TextField()
    v23_town = models.TextField()

    voter_score = models.TextField()

    def __str__(self):
        return f"{self.first_name} {self.last_name} registered {(self.party).strip()} from Precinct {self.precinct_num}"
    
    
    
def load_data():
    '''Function to load data records from CSV file into Django model instances.'''
    Voter.objects.all().delete()

    filename = '/Users/ethanliu/Downloads/newton_voters.csv'
    f = open(filename)
    headers = f.readline() # discard headers

    for line in f:
        
        try:          
            fields = line.split(',')
        # create a new instance of Result object with this record from CSV
            voter = Voter(
                        last_name = fields[1],
                        first_name = fields[2],
                        street_num = fields[3],
                        street_name = fields[4],
                        apt_num = fields[5],
                        zip_code = fields[6],
                        birthday = fields[7],
                        registration_date = fields[8],
                        party = fields[9].strip(),
                        precinct_num = fields[10],

                        v20_state = fields[11],
                        v21_town = fields[12],
                        v21_primary = fields[13],
                        v22_general = fields[14],
                        v23_town = fields[15],

                        voter_score = fields[16].strip(),
                    )
            print(f'Created result: {voter}')
            voter.save() # commit to database

        except:
            print(f"Skipped: {fields}")
    
    print(f'Done. Created {len(Voter.objects.all())} Results.')