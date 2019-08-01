#!/usr/bin/python
#
# Copyright 2018 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# Replace "pass" with your code

class BankAccount(object):
    def __init__(self, label, balance, withdraw, deposit):
        self.label = label
        self.balance = balance
        self.withdraw = withdraw
        self.deposit = deposit

    def bal(self):
        print("> You have %s in this %s account" % (self.balance, self.label))

    def wd(self):
        print("> You have withdrawn %s from your %s account" % (self.withdraw, self.label))
        if self.withdraw >= self.balance:
            print("> You cannot withdraw")
        else:
            self.balance = self.balance - self.withdraw
            print("> Your new balance is %s " % self.balance)

    def dep(self):
        print("> You have deposited %s from your %s account" % (self.deposit, self.label))
        if self.deposit <= 0:
            print(">You cannot deposit")
        else:
            self.balance = self.balance + self.deposit
            print(">Your new balance is %s " % self.balance)

myBankAccount = BankAccount("Wells Fargo", 50000, 5000, 10000)
myBankAccount.bal()
myBankAccount.wd()
myBankAccount.dep()
