import argparse
from datetime import datetime
import calendar

def calculate_difference(start_date, end_date):
    years = end_date.year - start_date.year
    months = end_date.month - start_date.month
    days = end_date.day - start_date.day

    if days < 0:
        months -= 1
        # Approximate days in previous month
        prev_month = start_date.replace(month=start_date.month % 12 + 1, day=1, year=start_date.year if start_date.month < 12 else start_date.year + 1)
        days_in_prev_month = (prev_month - start_date.replace(day=1)).days
        days += days_in_prev_month

    if months < 0:
        years -= 1
        months += 12

    return years, months, days

parser = argparse.ArgumentParser(description='Calculate date difference or show date details')
parser.add_argument('-s', '--start', nargs='+', help='Start date: day month year')
parser.add_argument('-e', '--end', nargs='+', help='End date: day month year')
parser.add_argument('-d', '--details', action='store_true', help='Show detailed information for dates')
parser.add_argument('-a', '--alone', nargs='+', help='Single date: day month year')

args = parser.parse_args()

if args.alone:
    date_str = ' '.join(args.alone)
    date = datetime.strptime(date_str, '%d %B %Y').date()
    day_of_year = date.timetuple().tm_yday
    week_of_year = date.isocalendar()[1]
    days_in_month = calendar.monthrange(date.year, date.month)[1]
    day_of_week = date.strftime('%A')
    current_date = datetime.now().date()
    age_years, _, _ = calculate_difference(date, current_date)
    print(f"Date - Day of year: {day_of_year}, Week of year: {week_of_year}, Days in month: {days_in_month}, Day of week: {day_of_week}, Age: {age_years}")
elif args.start and args.end:
    start_str = ' '.join(args.start)
    end_str = ' '.join(args.end)

    start_date = datetime.strptime(start_str, '%d %B %Y').date()
    end_date = datetime.strptime(end_str, '%d %B %Y').date()

    years, months, days = calculate_difference(start_date, end_date)
    print(f"Years: {years}, Months: {months}, Days: {days}")

    if args.details:
        def print_date_info(date, label):
            day_of_year = date.timetuple().tm_yday
            week_of_year = date.isocalendar()[1]
            days_in_month = calendar.monthrange(date.year, date.month)[1]
            day_of_week = date.strftime('%A')
            print(f"{label} - Day of year: {day_of_year}, Week of year: {week_of_year}, Days in month: {days_in_month}, Day of week: {day_of_week}")

        print_date_info(start_date, "Start date")
        print_date_info(end_date, "End date")
else:
    parser.error("Either provide -a for single date details or -s and -e for difference")