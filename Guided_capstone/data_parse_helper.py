import log_manager as log

# Function used to parse CSV data
def parse_csv(line):
    fields = line.split(',')
    if fields[2] == 'Q':
        trade_dt     = fields[0]
        rec_type     = fields[2]
        symbol       = fields[3]
        exchange     = fields[6]
        event_tm     = fields[1]
        event_seq_nb = fields[5]
        arrival_tm   = fields[4]
        trade_pr     = '-'
        bid_pr       = fields[7]
        bid_size     = fields[8]
        ask_pr       = fields[9]
        ask_size     = fields[10]
        execution_id = 'NA'
        trade_size   = 'NA'

    elif fields[2] == 'T':
        trade_dt     = fields[0]
        rec_type     = fields[2]
        symbol       = fields[3]
        exchange     = fields[6]
        event_tm     = fields[1]
        event_seq_nb = fields[5]
        arrival_tm   = fields[4]
        trade_pr     = fields[7]
        bid_pr       = '-'
        bid_size     = '-'
        ask_pr       = '-'
        ask_size     = '-'
        execution_id = 'NA'
        trade_size   = 'NA'

    # Rejected events
    else:
        log.log_rejected_rows(fields)

    return (trade_dt,
            rec_type,
            symbol,
            exchange,
            event_tm,
            event_seq_nb,
            arrival_tm,
            trade_pr,
            bid_pr,
            bid_size,
            ask_pr,
            ask_size,
            execution_id,
            trade_size)



# Function used to parse JSON data
import json
def parse_json(line):
    fields = json.loads(line)
    if fields['event_type'] == 'Q':
        trade_dt     = fields['trade_dt']
        rec_type     = fields['event_type']
        symbol       = fields['symbol']
        exchange     = fields['exchange']
        event_tm     = fields['event_tm']
        event_seq_nb = fields['event_seq_nb']
        arrival_tm   = fields['file_tm']
        trade_pr     = '-'
        bid_pr       = fields['bid_pr']
        bid_size     = fields['bid_size']
        ask_pr       = fields['ask_pr']
        ask_size     = fields['ask_size']
        execution_id = '-'
        trade_size   = '-'

    elif fields['event_type'] == 'T':
        trade_dt     = fields['trade_dt']
        rec_type     = fields['event_type']
        symbol       = fields['symbol']
        exchange     = fields['exchange']
        event_tm     = fields['event_tm']
        event_seq_nb = fields['event_seq_nb']
        arrival_tm   = fields['file_tm']
        trade_pr     = fields['price']
        bid_pr       = '-'
        bid_size     = '-'
        ask_pr       = '-'
        ask_size     = '-'
        execution_id = fields['execution_id']
        trade_size   = fields['size']

    # Rejected events
    else:
        log.log_rejected_rows(fields)

    return (trade_dt,
            rec_type,
            symbol,
            exchange,
            event_tm,
            event_seq_nb,
            arrival_tm,
            trade_pr,
            bid_pr,
            bid_size,
            ask_pr,
            ask_size,
            execution_id,
            trade_size)
