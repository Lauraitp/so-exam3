import psutil

class Stats():

  @classmethod
  def get_cpu_percent(cls):
    cpu_percent = psutil.cpu_percent()
    return cpu_percent

  @classmethod
  def get_available_memory_ram(cls):
    available_memory = psutil.virtual_memory().available
    return available_memory

  @classmethod
  def get_hard_disk_space(cls):
    disk_space = psutil.disk_usage('/').free
    return disk_space
