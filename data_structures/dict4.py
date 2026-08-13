trips = {
    "ub001":{'trip_id':'ub001','pickup':'chennai','drop':'airport','fare':475},
    "ub002":{'trip_id':'ub002','pickup':'tambaram','drop':'central','fare':410},
    "ub003":{'trip_id':'ub003','pickup':'medavakkam','drop':'t-nagar','fare':245}
    }


for trip,details in trips.items():
    print(trip)
    print(details['pickup'],"--->",details['drop'])
