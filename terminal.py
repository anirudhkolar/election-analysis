>>> type(3)
<class 'int'>
>>> type(tits)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'tits' is not defined
>>> type("tits")
<class 'str'>
>>> ballots(1,341)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'ballots' is not defined
>>> ballots = 1,341
>>> type(ballots)
<class 'tuple'>
>>> type(73.81)
<class 'float'>
>>> type(true)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'true' is not defined
>>> type(True)
<class 'bool'>
>>> num_candidates = 3
>>> winning_percentage = 73.81
>>> candidate = "Diane"
>>> won_election = True
>>> type(num_candidates)
<class 'int'>
>>> 5+2*3
11
>>> 
>>> 5+2*3
11
>>> 8 // 5 - 3
-2
>>> 8//5
1
>>> 8 + 22 * 2 - 4
48
>>> 16 - 3/2 + 7 - 1
20.5
>>> 3 ** 3 % 5
2
>>> 3 % 5
3
>>> 5 % 3
2
>>> counties = ["Arapahoe", "Denver", "Jefferson"]
>>> counties
['Arapahoe', 'Denver', 'Jefferson']
>>> counties[0]
'Arapahoe'
>>> print(counties[0])
Arapahoe
>>> counties[-1]
'Jefferson'
>>> counties[-3]
'Arapahoe'
>>> counties[-2]
'Denver'
>>> len(counties)
3
>>> len(counties{-2])
  File "<stdin>", line 1
    len(counties{-2])
                ^
SyntaxError: invalid syntax
>>> len(counties[1])
6
>>> counties[0:2]
['Arapahoe', 'Denver']
>>> counties[0:3]
['Arapahoe', 'Denver', 'Jefferson']
>>> counties[0:4]
['Arapahoe', 'Denver', 'Jefferson']
>>> counties[0:]
['Arapahoe', 'Denver', 'Jefferson']
>>> counties[:2]
['Arapahoe', 'Denver']
>>> counties[:3]
['Arapahoe', 'Denver', 'Jefferson']
>>> counties.append("append")
>>> counties
['Arapahoe', 'Denver', 'Jefferson', 'append']
>>> counties.remove("append")
>>> counties.append("El Paso")
>>> counties
['Arapahoe', 'Denver', 'Jefferson', 'El Paso']
>>> counties.insert(2, "Santa Clara")
>>> counties
['Arapahoe', 'Denver', 'Santa Clara', 'Jefferson', 'El Paso']
>>> counties.pop(-1)
'El Paso'
>>> counties.pop(2)
'Santa Clara'
>>> counties
['Arapahoe', 'Denver', 'Jefferson']
>>> counties[2] = "El Paso"
>>> counties
['Arapahoe', 'Denver', 'El Paso']
>>> counties[1] = "El Paso"
>>> counties
['Arapahoe', 'El Paso', 'El Paso']
>>> counties.remove("Arapahore")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: list.remove(x): x not in list
>>> counties.remove("Arapahoe")
>>> counties
['El Paso', 'El Paso']
>>> counties.insert(2, "Denver")
>>> counties.pop(0)
'El Paso'
>>> counties.insert(1, "Jefferson")
>>> counties.append("Arapahoe")
>>> counties
['El Paso', 'Jefferson', 'Denver', 'Arapahoe']
>>> 
>>> 
>>> 
>>> 
>>> 
>>> counties_tuple("Arapahoe", "Denver", "Jefferson")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'counties_tuple' is not defined
>>> counties_tuple = ("Arapahoe", "Denver", "Jefferson")
>>> counties_tuple
('Arapahoe', 'Denver', 'Jefferson')
>>> len(counties_tuple)
3
>>> 
>>> 
>>> 
>>> counties_dict
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'counties_dict' is not defined
>>> counties_dict = {}
>>> counties_dict["Arapahoe"] = 422829
>>> counties_dict["Denver"] = 463353
>>> counties_dict["Jefferson"] = 432438
>>> counties_dict
{'Arapahoe': 422829, 'Denver': 463353, 'Jefferson': 432438}
>>> len(counties_dict)
3
>>> count_dict
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'count_dict' is not defined
>>> counties_dict
{'Arapahoe': 422829, 'Denver': 463353, 'Jefferson': 432438}
>>> counties_dict.items()
dict_items([('Arapahoe', 422829), ('Denver', 463353), ('Jefferson', 432438)])
>>> counties_dict.keys
<built-in method keys of dict object at 0x7fd48a8759b0>
>>> counties_dict.keys()
dict_keys(['Arapahoe', 'Denver', 'Jefferson'])
>>> counties_dict.values()
dict_values([422829, 463353, 432438])
>>> counties_dict.get("Denver")
463353
>>> counties_dict.get(463353)
>>> counties_dict.get()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: get expected at least 1 arguments, got 0
>>> counties.dict[1]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'list' object has no attribute 'dict'
>>> counties.dict["Arapahoe"]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'list' object has no attribute 'dict'
>>> counties_dict["Arapahoe"]
422829
>>> voting_data = []
>>> voting_data.append({"county":"Arapahoe", "registered_voters": 422829})
>>> voting_data.append({"county":"Denver", "registered_voters": 463353})
>>> voting_data.append({"county":"Jefferson", "registered_voters": 432438})
>>> voting_data.append
<built-in method append of list object at 0x7fd48a936dc0>
>>> voting_data
[{'county': 'Arapahoe', 'registered_voters': 422829}, {'county': 'Denver', 'registered_voters': 463353}, {'county': 'Jefferson', 'registered_voters': 432438}]
>>> voting_data.insert(1, {"county":"El Paso", "registered_voters": 461149})
>>> voting_data.remove({"county":"Arapahoe", "registered_voters": 422829})
>>> voting_data.remove({"county":"Denver", "registered_voters": 463353})
>>> voting_data.append({"county":"Denver", "registered_voters": 463353})
>>> voting_data
[{'county': 'El Paso', 'registered_voters': 461149}, {'county': 'Jefferson', 'registered_voters': 432438}, {'county': 'Denver', 'registered_voters': 463353}]
>>> voting_data.append({"county":"Arapahoe", "registered_voters": 422829})
>>> 
>>> voting_data
[{'county': 'El Paso', 'registered_voters': 461149}, {'county': 'Jefferson', 'registered_voters': 432438}, {'county': 'Denver', 'registered_voters': 463353}, {'county': 'Arapahoe', 'registered_voters': 422829}]
>>> 
