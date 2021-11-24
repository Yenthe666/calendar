# calendar
Apps related to Odoo it's calendar/appointments features:
- [online_appointment_locations](#online_appointment_locations): allow setting an online URL per employee


## online_appointment_locations
Adds support to set an online URL per employee. This way you can use URL's to meeting rooms from Hangouts, Zoom, Microsoft Meet etc.<br/>
This allows the "website_calendar" module to be a little more future-proof by allowing online (call) URL's:
![image](https://user-images.githubusercontent.com/6352350/143216117-35ad3897-a447-439e-a6ce-2ee0151c9297.png)

When the employee has an "Online appointment URL" set we will insert this as the location into the e-mail sent to the customer.<br/>
If no URL is set on the employee we will fallback to the default "Location" set on the online appointment type.
