# PYTHON3

# Retourner le titre universitaire et le nom de famille des personnes dans la liste

people = ['Dr. Christopher Brooks', 'Dr. Kevyn Collins-Thompson', 'Dr. VG Vinod Vydiswaran', 'Dr. Daniel Romero']

def split_title_and_name(person):
    title = person.split(' ')[0]
    name = person.split(' ')[-1]
    title_name = title + ' ' + name
    return title_name

list(map(split_title_and_name, people))
