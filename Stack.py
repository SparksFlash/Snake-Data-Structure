# LIFO Behaviour

browsing_session = []
browsing_session.append(1)
browsing_session.append(2)
browsing_session.append(3)
print(browsing_session)
last = browsing_session.pop()
print(last)
print("Redirect", browsing_session[-1])
if not browsing_session:
    browsing_session[-1]
