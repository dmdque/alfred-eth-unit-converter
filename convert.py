import sys
from workflow import Workflow3


def main(wf):
    unit = None
    query = None
    for i, arg in enumerate(sys.argv):
        if arg == '--wei':
            unit = 'wei'
            query = sys.argv[i + 1]
        elif arg == '--gwei':
            unit = 'gwei'
            query = sys.argv[i + 1]
        elif arg == '--eth':
            unit = 'eth'
            query = sys.argv[i + 1]

    if unit == 'wei':
        etherValue = float(query) / 10**18
        etherDict = {'title': str(etherValue), 'subtitle': 'ether', 'valid': True, 'arg': str(etherValue)}
        wf.add_item(**etherDict)

        gweiValue = float(query) / 10**9
        gweiDict = {'title': str(gweiValue), 'subtitle': 'gwei', 'valid': True, 'arg': str(gweiValue)}
        wf.add_item(**gweiDict)

    elif unit == 'gwei':
        weiValue = float(query) * 10**9
        weiDict = {'title': str(weiValue), 'subtitle': 'wei', 'valid': True, 'arg': str(weiValue)}
        wf.add_item(**weiDict)

        etherValue = float(query) / 10**9
        etherDict = {'title': str(etherValue), 'subtitle': 'ether', 'valid': True, 'arg': str(etherValue)}
        wf.add_item(**etherDict)
    elif unit == 'eth':
        weiValue = float(query) * 10**18
        weiDict = {"title": str(weiValue), "subtitle": "wei", "valid": True, "arg": str(weiValue)}
        wf.add_item(**weiDict)

        gweiValue = float(query) * 10**9
        gweiDict = {"title": str(gweiValue), "subtitle": "gwei", "valid": True, "arg": str(gweiValue)}
        wf.add_item(**gweiDict)

    wf.send_feedback()


if __name__ == '__main__':
    wf = Workflow3()
    sys.exit(wf.run(main))
