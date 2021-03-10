# write your code here
with open('salary.txt') as salary, \
        open('salary_year.txt', 'w') as year_salary:

    for line in salary:
        payment = int(line.strip())
        yearly_payment = str(int(payment) * 12)
        year_salary.write(yearly_payment + '\n')
