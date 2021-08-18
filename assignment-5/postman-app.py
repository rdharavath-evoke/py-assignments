from flask import Flask,request
appFlask = Flask(__name__)

    
@appFlask.route('/getloandetails', methods=['POST'])
def getloandetails():
    return homeloan()

def homeloan():
    request_data = request.get_json()
    amount = request_data['loan amount']
    time=request_data['Tenure(no.of Years)']
    rate=rates(amount)
    
    if amount<9000000:
        total_interest=simple_interest(amount, time, rate)
        total_amount=total_interest+amount
        return {"Total-Interst":total_interest,"Total-Amount":total_amount}
    else:
        return {"more than 90Laks there is no homeloans ":
                "please select the amount less than 90Lakhs"}

def rates(amount):
        try:
            if amount<=3000000:
                rate=6.5
                return rate
            elif 3000000<amount<=5000000:
                rate=7.5
                return rate
            elif 5000000<amount<=9000000:
                rate=9.0
                return rate
        except Exception: 
            return '''More than 90Laks, there is no loans'''
        
def simple_interest(p,t,r):
        si = (p * t * r)/100
        return si


if __name__ == '__main__':
    appFlask.run(debug = True)