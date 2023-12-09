from parseInput import parseInput

class Monkey:
    def __init__(self, id):
        self.id = id
        self.items = []
        self.worryLevelOp = ''
        self.worryLevelVal = None
        self.testOpVal = None
        self.trueMonkeyID = id
        self.falseMonkeyID = id
        self.inspected_count = 0

    def processOperation(self,element):
        operation = element[1:]
        operator = operation[3]
        if operation[4] == 'old':
            # Multiply by self
            value = 'old'
        else: 
            value = int(operation[4])
        self.worryLevelOp = operator
        self.worryLevelVal = value

    def loadItems(self,element):
        for i, part in enumerate(element):
            if i >= 2:
                self.items.append(int(part.replace(',','')))

def completeOperation(old_value, operator, value):
    if operator == '*':
        new_value = old_value * value
    elif operator == '+':
        new_value = old_value + value
    else:
        raise(ValueError('This operator doesnt exist'))
    return new_value

def executeOperation(old_value, operator, value):
    if value == 'old':
        value = old_value
        new_value = completeOperation(old_value, operator, value)
    else:
        new_value = completeOperation(old_value, operator, value)
    return new_value

def itemTransaction(receiver_id, monkeys, item_value):
    for monkey in monkeys:
        if receiver_id == monkey.id:
            monkey.items.append(item_value)
            break

if __name__ == "__main__":
    input_lines = parseInput()
    monkeys = []
    for element in input_lines:
        if element[0] != '': # new element
            if element[0] == 'Monkey':
                curr_id = int(element[1].replace(':',''))
                monkeys.append(Monkey(curr_id))
            elif element[0] == 'Starting':
                monkeys[-1].loadItems(element)
            elif element[0].replace(':','') == 'Operation':
                monkeys[-1].processOperation(element)
            elif element[0].replace(':','')  == 'Test':
                monkeys[-1].testOpVal = int(element[3])
            else: 
                if element[1].replace(':','')  == 'true':
                    monkeys[-1].trueMonkeyID = int(element[5])
                else:
                    monkeys[-1].falseMonkeyID = int(element[5])

    # Process rounds
    count = 0
    continue_bool = True
    while continue_bool:
        for monkey in monkeys:
            if len(monkey.items) == 0:
                count += 1
                continue
            else:
                for i, item in enumerate(monkey.items):
                    if item == -1:
                        continue
                    monkey.inspected_count += 1
                    new_value = executeOperation(item, monkey.worryLevelOp, monkey.worryLevelVal)
                    new_value = new_value // 3
                    if new_value % monkey.testOpVal == 0:
                        # Throw item to True monkey trueMonkeyID
                        itemTransaction(monkey.trueMonkeyID, monkeys, new_value)
                        monkey.items[i] = -1
                    else:
                        # Throw item to False monkey falseMonkeyID
                        itemTransaction(monkey.falseMonkeyID, monkeys, new_value)
                        monkey.items[i] = -1
        count += 1
        if count == 20:
            continue_bool = False
            break
    inspected_list = []
    for monkey in monkeys:
        inspected_list.append(monkey.inspected_count)
    inspected_list.sort()
    print(inspected_list[-1]*inspected_list[-2])