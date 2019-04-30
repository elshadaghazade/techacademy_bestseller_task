def parse_file(file):
    with open(file, "r") as f:
        # result = []
        for line in f:
            line = line.strip().split("\t")
            title, author, publisher, release, genre = line
            
            release_date = release.strip().split("/")

            year = int(release_date[-1])
            month = int(release_date[-3])
            day = int(release_date[-2])

            yield author, title, publisher, release.strip(), genre, year, month, day

        # return result

def find_by_year_range(file, from_year, to_year):
    print(f"All Titles between {from_year} and {to_year} :")

    for author, title, publisher, release_date, genre, year, month, day in parse_file(file):
        if year >= from_year and year <= to_year:
            print(f"{title} ({release_date})")


def find_by_month_year(file, p_month, p_year):
    print(f"All Titles in month {p_month} of {p_year} :")
    for author, title, publisher, release_date, genre, year, month, day in parse_file(file):
        if year == p_year and month == p_month:
            print(f"{title} ({release_date})")


def find_by_title(file, p_title):
    for author, title, publisher, release_date, genre, year, month, day in parse_file(file):
        if p_title.lower() in title.lower():
            print(f"{title} ({release_date})")


def find_by_author(file, p_author):
    for author, title, publisher, release_date, genre, year, month, day in parse_file(file):
        if p_author.lower() in author.lower():
            print(f"{title} | {author} ({release_date})")