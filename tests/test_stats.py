import pytest
import sys
sys.path.append('/home/laura-exam3/so-exam3')

from op_stats.app import app
from op_stats.stats import Stats

@pytest.fixture
def client():
  client = app.test_client()
  return client

def test_get_cpu_percent(mocker, client):
  mocker.patch.object(Stats, 'get_cpu_percent', return_value=100)
  response = client.get('/cpu')
  assert response.data.decode('utf-8') == '{"cpu_percent": 100}'
  assert response.status_code == 200

def test_get_available_memory(mocker, client):
  mocker.patch.object(Stats, 'get_available_memory_ram', return_value=2000)
  response = client.get('/memory')
  assert response.data.decode('utf-8') == '{"available_memory(MB)": 2000}'
  assert response.status_code == 200


def test_get_disk_space(mocker, client):
  mocker.patch.object(Stats, 'get_hard_disk_space', return_value=1000)
  response = client.get('/disk')
  assert response.data.decode('utf-8') == '{"disk_space(MB)": 1000}'
  assert response.status_code == 200
