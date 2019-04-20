import random
from nlu_functions.entity import extract_entity_names
import requests

import json



def hello(query):
    if len(query.split()) < 3:
        msg1 = random.choice(["Hi", "", "Hello", "What\'s up!", "Bonjour"])
    
    msg = '''Hello, I'll guide you through the admissions!'''+msg1;
    return msg

def programme(query):
     msg='''B. Tech., 5- Year integrated M.Tech., M. Tech.,<br> MCA, MBA, B.Com. (CA),B.Com. (BFSI), B.A./B.Com./B.B.A., LL.B, (Hons.),<br>
     B.Sc./B.A., B.Ed. (4-year integrated) & M.Sc.  (5-year integrated)
     programmes in its Main Campus in Thanjavur <br> <br>B. Sc., B.Com, BBA, BCA, M.Sc., and B. Tech. (CSE, ECE, EEE,) courses 
     in its Srinivasa Ramanujan Centre (off-campus centre of SASTRA recognized by Govt. of India) in Kumbakonam''';
     return msg;

def form(query):
    msg='''Application forms will be available online from April 12,2019<br>
    Please note that all downloaded applications must be filled and submitted with the necessary
    application fee to be considered for admissions <br>
    Rs.650/- for B.Tech / M.Tech.(5-Year intg.) / M.Tech. / Law - (5-Year integrated) / M.C.A. (Regular / Lateral Entry) / M.B.A)<br> 
    Rs.350/- for B.Sc. / B.B.A. / B.C.A / B.Com. / B.F.A., (Music) / M.Com. / M.Sc. / B.Sc.,B.Ed., & B.A.,B.Ed. /  B.Com.(CA) / B.Com. (BFSI) / M.Sc.(5-Year intg.) / B.Optom). <br>
    On receipt of the filled application form and fee, the applicant will be intimated of the application number by e-mail.<br> 
    The application number is a unique ID for any future reference. Applicants will also be sent a copy of the brochure
    to the mailing address in the application form. <br>
    Application fee must be in the form of DD favouring SASTRA payable at Thanjavur.<br>
    The Hard Copy will be available in the Store";'''
    return msg;

def dl(query):
    msg="Click to download here <a href='http://sastra.edu/adm2019/'>Application form</a>";
    return msg;

def proc(query):
    msg='''Admission to the B.Tech. / 5-year Integrated M.Tech. programs will be conducted under two streams.<br>
    All the applicants will be eligible for both the streams and need not submit two separate application forms.<br>
    This application will be considered for the both streams.<br>
    (1) Stream 1 (based on JEE(Main) 2019 scores and +2 Marks) for 70% of seats<br>
    (2) Stream 2 (based on +2 marks) for 30% of seats''';
    return msg;

def hos(query):
    msg='''There are 9 hostels for boys and 5 for girls.<br>
    First year B. Tech. students will be provided shared accommodation
    at an annual rent of Rs.10,000 only.<br>
    The charges for food will be at actual based on dividing system 
    and will approximately be around Rs.3,000 per month.<br>
    You can assume that you will stay for 10 months in a calendar year. 
    Single room, Two-in-one, Three-in-one and Four-in-one (with or w/o bath attached facilities)<br>
    will be available from II year onwards. The annual rent will be different.''';
    return msg;

def fees(query):
    msg='''Click to check <a href='https://www.sastra.edu/index.php/2014-01-29-07-16-11/tuition-fees/fee-structure.html'>Fees</a> here''';
    return msg;

def nri(query):
    msg='''As per the Government norms, provision is made for NRI admissions.<br>
     Interested students may kindly contact the Office of admissions at <a href='tel:91 4362 304102'>91 4362 304102.</a> ''';
    return msg;

def con(query):
    msg='''Please contact the Office of Admissions for any additional information that you may require.<br>
     Kindly ensure you talk to the right person and do not be guided by outsider or any unauthorized person. <br>
     Ask for the following persons:<br>

     Mr.C.Swaminathan (Deputy Registrar)<br>

     Mr.G.Ganapathi<br>subramanian(Deputy Registrar)<br>

     Mr.S.Radhakrishnan (Office of the VC)<br>

     Mr.A.Sahayaraj (Asst. Registrar for PG & Law admissions)<br>

      Mr.S.Rajagopalan, Admin Officer, SRC, Kumbakonam at 0435 2426823 for   SRC admissions<br>
      Phone: <a href='tel:91 4362 264101'>91 4362 264101</a>/
      <a href='tel:304000-010'>304000-010</a>''';
    return msg;

def stop(query):
    return "  We wish you good luck and welcome to a world of opportunities at SASTRA!"

