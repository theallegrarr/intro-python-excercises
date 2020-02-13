class Worker:
  def __init__(self, name, rate):
    self.name = name
    self.rate = rate

  def hourly_rate(self):
    return self.rate

class HourlyPolicy:
  def __init__(self, hours_worked, hour_rate, name):
    self.hours_worked = hours_worked
    self.worker = Worker(name, hour_rate)

  def calculate_payroll(self):
    return f" Salary for worker is {self.hours_worked * self.worker.hourly_rate}"