import pyodin as odin
import unittest
from pymongo import MongoClient
import json
from os import environ
import random


class odinSdkTest(unittest.TestCase):
    def setUp(self):
        client = MongoClient(environ.get('ODIN_MONGODB'))
        mongodb = client['odin']
        self.collection = mongodb['observability']

    def tearDown(self):
        self.collection.delete_many({"id" : "test_id"})

    def testConditionNotOdinEnv(self):
        r = random.randint(100000, 999999)
        test_desc = 'test_desc' + str(r)
        
        o = odin.Odin(config="job.yml", pathType="relative")

        cond = o.condition(test_desc, True)       
        result = self.collection.find_one({"description" : test_desc})
    
        self.assertEqual(cond, True) 
        self.assertEqual(None, result)

    def testWatchNotOdinEnv(self):
        r = random.randint(100000, 999999)
        test_desc = 'test_desc' + str(r)
        
        o = odin.Odin(config="job.yml", pathType="relative")

        o.watch(test_desc, True)
        result = self.collection.find_one({"description" : test_desc})

        self.assertEqual(None, result)

    def testCondition(self):
        r = random.randint(100000, 999999)
        test_desc = 'test_desc' + str(r)
        
        # test True sets odin exc env to true and in turn enables logging everything to the DB
        o = odin.Odin(test=True, config="job.yml", pathType="relative")

        cond = o.condition(test_desc, True)
        result = self.collection.find_one({"description" : test_desc})

        self.assertEqual(cond, True)    
        self.assertEqual(test_desc, result['description'])

    def testWatch(self):
        r = random.randint(100000, 999999)
        test_desc = 'test_desc' + str(r)
        
        # test True sets odin exc env to true and in turn enables logging everything to the DB
        o = odin.Odin(test=True, config="job.yml", pathType="relative")

        o.watch(test_desc, True)       
        result = self.collection.find_one({"description" : test_desc})
        
        self.assertEqual(test_desc, result['description'])


if __name__ == "__main__":
    unittest.main() # run all tests
