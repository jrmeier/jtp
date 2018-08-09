import re
import sys

# read the file line by line
def verify_inputs(logic_obj, ind, obj):
    # check the base
    
    if logic_obj['operator'] not in ['>','>=','<','<=','=']:
        return False
    
    if logic_obj['aux'] not in ind:
        print("undefined indicator in {0} aux: ".format(obj, logic_obj['aux']))
        return False
     
    if logic_obj['base'] not in ind:
        print("undefined indicator in {0} base: {1}".format(obj, logic_obj['base']))
        return False
    
    return True

def build_file(strategy):
    # only interested in the logic
    lines_to_write = []    
 
    lines_to_write.append("def buy(curr_data, history):")
     
    for each in strategy['buy']['logic']:
        inputs = verify_inputs(each, strategy['ind'], "buy")
        if not inputs:
            return False
        line = "\n\tif {0} {1} {2}:".format(each['base'], each['operator'], each['aux'])
        lines_to_write.append(line)
        line = "\n\t\t return True"
        lines_to_write.append(line) 
        

    lines_to_write.append("\n\ndef sell(curr_data, history):")
    for each in strategy['sell']['logic']:
        inputs = verify_inputs(each, strategy['ind'], "sell")
        line = "\n\tif curr_data['{0}'] {1} curr_data['{2}']:".format(each['base'], each['operator'], each['aux'])
        lines_to_write.append(line)
        line = "\n\t\t return True"
        lines_to_write.append(line)
    
    for line in lines_to_write:
        print(line)
    
    return
    with open(strategy['name']+'.py', 'w') as f:
        for line in lines_to_write:
            f.write(line)
if __name__ == "__main__":
    ap_file = sys.argv[1]
    import json
    with open(ap_file, 'r') as f:
        strategy = json.load(f)
        build_file(strategy)

