"""
Builds the dataset for the Enso Group HR Policy Manual (79 pages)
and creates data/hr_manual_extracted.json and data/hr_manual.pdf
"""
import os
import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"
DATA_DIR.mkdir(parents=True, exist_ok=True)

# 79 Pages of the Enso Group HR Policy Manual
PAGES_DATA = [
    {
        "page": 1,
        "section": "Cover",
        "title": "Enso Group HR Manual - Cover",
        "content": "ENSO GROUP\nHR MANUAL\nEnso Group Human Resources Policy Manual"
    },
    {
        "page": 2,
        "section": "Table of Contents",
        "title": "Contents - Part 1",
        "content": """Contents
Introduction
Section 1: Employing Staff (Page 5)
1.1 Recruitment (Page 6)
1.2 Induction Policy (Page 6)
1.3 Employee's Employment (Page 8)
1.4 Standards of business Conduct (Page 9)
1.5 Internet and email usage policy and guidelines (Page 12)

Section 2: Managing Employee Performance (Page 16)
2.1 Performance Appraisal Policy (Page 17)
2.2 Controlling Absence Policy (Page 18)
2.3 Disciplinary Procedure (Page 19)
2.4 Capability Procedure (Page 21)

Section 3: Dealing with Employee Concerns (Page 22)
3.1 Grievance Procedure (Page 23)
3.2 Prevention of Bullying and Harassment at Work (Page 25)
3.3 Whistleblowing Policy - Making a Disclosure in the Public Interest (Page 26)

Section 4: Supporting Our Staff in the Workplace (Page 28)
4.1 Equality Policy (Page 29)
4.2 Drug and Alcohol Abuse Policy (Page 31)
4.3 Health and safety policy (Page 31)

Company Rules and regulation (Page 34)

Annexure - I (Page 39)
a. On boarding process (Page 40)
b. Probation policy (Page 42)
c. Training and development (Page 44)
d. Relocation policy (Page 45)
e. Off boarding policy (Page 46)

Annexure - II (Page 48)
a. Equal Opportunities (Page 50)
b. Data card/Visiting Cards/Emails Policy (Page 51)

Annexure III (Page 52)
a. Dress code (Page 53)
b. Work timing policy (Page 54)
c. Punctuality and attendance (Page 55)
d. Compensation policy (Page 57)
e. Staff advances (Page 58)
f. Employment Of Relatives Policy (Page 59)
g. Leave policy (Page 60)
h. Reward and recognition (Page 63)
i. Whistle Blower Policy & Anti Sexual Harassment Policy (Page 64)"""
    },
    {
        "page": 3,
        "section": "Table of Contents",
        "title": "Contents - Part 2",
        "content": """Contents
Annexure IV (Page 66)
a. Long distance travel policy (Page 67)
b. Short distance travel policy (Page 73)"""
    },
    {
        "page": 4,
        "section": "Introduction",
        "title": "Introduction to Enso Group HR Policy Manual",
        "content": """Introduction
Enso Group HR Policy Manual
This Human Resources Policy Manual is provided as a central reference for all managers, supervisors and employees and applies to staff across all locations where the Company carries out its work.
The specific policies that follow promote the philosophy of Enso Group with regard to standards of excellence; terms of employment; employee development; and employee services.
It may be necessary to change these policies from time to time to reflect changes in the workforce, employment trends, economic conditions and Global legislation. However, any changes in policy will be consistent with the Company's approach to:
- Employing talented individuals whose creativity and imagination will support and contribute to achieving Company's business objectives;
- Communicating Company standards and expectations in all aspects of employment including performance;
- Valuing diversity, and assure equal employment opportunity and a workplace where relationships are based on mutual respect;
- Treating all staff, workers, contractors and customers in a professional, non-discriminatory manner;
- Providing safe, effective working conditions, and;
- Providing competitive terms and conditions in our workplace market.
Any Policy changes will be fully consulted on and communicated to all staff through normal communication channels. This Policy Manual will also be updated as necessary. This Manual applies to all Jurisdictions Globally."""
    },
    {
        "page": 5,
        "section": "Section 1",
        "title": "Section 1 - Employing Staff",
        "content": """SECTION - I
EMPLOYING STAFF
Employing staff fairly, and ensuring they are aware of the required standards of business conduct including use of email and the internet."""
    },
    {
        "page": 6,
        "section": "Section 1.1 & 1.2",
        "title": "Recruitment & Induction Policy",
        "content": """Recruitment - Introduction
Effective recruitment and selection is central and crucial to the successful functioning of Enso Group. It depends on finding people with the necessary skills, expertise and qualifications to deliver the Company's strategic objectives and the ability to make a positive contribution to the values and aims of the organisation.

Advertisement:
- Vacancies will generally be advertised in an appropriate newspaper or journal, and will not be confined to those media which provide only or mainly applicants of a particular group.
- Advertisements will also be notified to the local job centre.
- Enso Group may, on occasions, decide to restrict advertisement to internal candidates only.
- In applying for posts, all candidates will be provided with a job description, details of the appropriate conditions of service and details about the Company.
- The Company will ensure that no job Candidate receives less favourable treatment than another on the grounds of disability, gender, race, religion or belief, age, sexual orientation, marital status, parental status, caring responsibilities or hours of work.
- Candidates will be asked to specify whether they have any disabilities, and whether there are any reasonable adjustments needed.
- All candidates will be asked to declare whether they have ever been convicted of any criminal offence which cannot be regarded as 'spent'.
- Applicants will also be required to declare if they are related to any member of staff within the Company. Canvassing of members of the Company is not permitted.
- A short-list of candidates will be drawn up for interview, based entirely on merit and suitability for the post.

Induction Policy - General Policy Statement
Enso Group believes that all new employees MUST be given timely induction training. This training is regarded as a vital part of staff recruitment and integration into the working environment. This policy defines the Company's commitment to ensure that all staff is supported during the period of induction."""
    },
    {
        "page": 7,
        "section": "Section 1.2",
        "title": "Induction Policy - Aim & Guidelines",
        "content": """Induction Policy - Aim
It is the aim of the Company to ensure that staff induction is dealt with in an organised and consistent manner, to enable staff to be introduced into a new post and working environment quickly, so that they can contribute effectively as soon as possible.
Implementation of good induction practice by managers/supervisors will:
- Enable new employees to settle into the Company quickly and become productive and efficient.
- Ensure that new entrants are highly motivated and that this motivation is reinforced.
- Assist in reducing staff turnover, lateness, absenteeism and poor performance generally.
- Assist in developing a management style where the emphasis is on leadership.
- Ensure that employees operate in a safe working environment.
- Reduce costs associated with repeated recruitment, training and lost production.

The Company's Commitment:
The Company Human Resources Department / Head Office will:
- Issue guidelines to familiarise managers and staff with the induction process.
- Maintain and update the Induction Policy.
- Provide a checklist for managers and staff to follow during the induction period.
- Deal with any problems promptly and provide relevant formal training courses."""
    },
    {
        "page": 8,
        "section": "Section 1.3",
        "title": "Employee's Employment & Payroll",
        "content": """First Day of Employment:
Preparations should be made for the arrival of the new entrant well in advance (desk, equipment, lockers). An introductory talk will be conducted and a tour of the workplace arranged.

Employee's Employment - Introduction:
Employees Employment in Enso Group is essentially governed by Contract of Employment, Enso Group policies.

Payroll:
- Employees pay cycle will be monthly. Pay will be automatically deposited electronically into the bank account details provided to Enso Group.
- Taxation payments will be automatically deducted from the salary.
- The company shall review the employee's salary on the first anniversary of the employment and at six monthly intervals thereafter for the remaining term of the employment, but shall be under no obligation to increase the salary.
- The company shall be entitled to deduct from the employee's salary or other payments due to an employee any payment which he/she owe the company at any time.
- Employee will be eligible to participate in the company's discretionary bonus scheme. The award of any bonus and its amount will be at the company's discretion and will be paid once each year in such month as the company shall announce.

Changing Pay Details:
Employee will have to advise the Human Resource Department via email should he/she wish to change any details like changing or closing the bank account."""
    },
    {
        "page": 9,
        "section": "Section 1.3 & 1.4",
        "title": "Lateness for Work, Travel & Standards of Business Conduct",
        "content": """Lateness for Work:
Any absence or late arrival due to illness, injury or any other reason, and the unexpected duration of leave must be personally reported to the supervisor as soon as practicable.

Reimbursement of expenses:
Enso Group will reimburse employees for pre-approved expenses properly incurred in the proper performance of their duties upon providing receipts or other evidence.

Travel:
Reasonable Travelling Expenses incurred in performance of duties will be reimbursed with prior authorisation. Generally air travel will be by economy class, with carrier chosen by Enso Group.

Standards of Business Conduct - Introduction:
Enso Group expects its staff (including temporary, agency, interim, contractor or consultant staff) to be scrupulously impartial and honest.
The duties of an employee are:
- To be ready and willing to work;
- To offer their services personally (must not subcontract work);
- To take reasonable care, be competent at work and take care of Company property;
- To not wilfully disrupt Company business;
- To obey reasonable orders;
- To work only for the Company in Company's time;
- To disclose information relevant to Company business;
- To hold solely for the Company the benefit of any invention;
- To respect trade secrets and be of good faith;
- To account for all benefits received;
- To indemnify the employer for loss caused by the employee."""
    },
    {
        "page": 10,
        "section": "Section 1.4",
        "title": "Standard of Conduct Required by the Company",
        "content": """Standard of Conduct Required by the Company:
Gifts and Hospitality:
The Company requires its employees to ensure that gifts and hospitality offered by suppliers are declined. Trivial gifts with a nominal value such as a calendar, diary, chocolates or mugs can be accepted. All other gifts must be politely refused or returned.

Transaction of Private Business:
Employees must avoid transacting any kind of private business with contractors or suppliers other than through normal commercial channels.

Visits to Conferences, Demonstrations:
The Company will bear travelling and subsistence expenses itself for approved visits.

Attendance at Luncheons, Receptions:
Invitations may be accepted only with prior approval of Department Manager.

Identification:
Employees should wear or carry their identity badges whilst carrying out duties.

Confidentiality:
Confidentiality must be maintained at all times. No information can be released to unauthorised persons.

Personal Relationships:
If a personal relationship develops between two employees, the senior employee must bring this to the attention of the manager to confirm there is no conflict of interest."""
    },
    {
        "page": 11,
        "section": "Section 1.4",
        "title": "Outside Interests, Bribery and General Conduct",
        "content": """Outside Interests and Employment:
Outside interests including directorships, ownership, or material shareholdings in companies likely to do business with Enso Group must be declared to line manager.

Political and civic activities:
No Company employee should permit company affiliation to be noted in outside organisation's materials without express written approval.

Bribery and Corruption:
The Company has a strict anti-bribery and corruption policy. A bribe is defined as giving someone a financial or other advantage to encourage improper performance. Bribing or accepting a bribe is gross misconduct resulting in disciplinary action up to and including dismissal.

General Conduct:
Employees should conduct themselves to enhance the reputation of the Company. Whistleblowing disclosures will be supported."""
    },
    {
        "page": 12,
        "section": "Section 1.5",
        "title": "Internet and Email Usage Policy and Guidelines",
        "content": """Internet and Email Usage Policy and Guidelines:
Introduction: Sets out obligations for IT facilities for internet and email.
Authorisation: Only authorised persons may use Company IT facilities.
Legislation: Users must comply with Data Protection, Computer Misuse, Copyright Design and Patents, Defamation, and Terrorism legislation.
Responsibilities: Users must act in a manner that will not cause damage or disrupt services. Users are responsible for any IT activity initiated under their username."""
    },
    {
        "page": 13,
        "section": "Section 1.5",
        "title": "Use of Internet and Email Rules",
        "content": """Use of the Internet:
- Must not participate in online activities likely to bring the Company into disrepute.
- Must not visit, view or download illegal or inappropriate material (pornography, hate material, gambling, illegal drugs).
- Must not introduce computer viruses or hack into unauthorised areas.
- Must not use internet for personal financial gain or criminal activities.
- Limited personal use allowed only during non-work time (e.g. lunch-time).
- Social networking sites (Facebook, LinkedIn, Twitter, YouTube) are not permissible.

Use of Email:
- Do not disrupt wider IT systems with large attachments.
- Do not use email for offensive, abusive, discriminatory, or harassing messages.
- Do not send chain letters or joke emails from Company account.
- Personal use of Company email is not permitted."""
    },
    {
        "page": 14,
        "section": "Section 1.5",
        "title": "Email Good Practice & Virus Protection",
        "content": """Good Practice:
- Guidelines for email when out of office for longer than 3 days: activate out-of-office facility naming an alternative contact.
- Tone must be businesslike and appropriate.
- Delete personal and unsolicited junk mail.
- Automatic virus checker is provided; it is a disciplinary offence to disable the virus checker."""
    },
    {
        "page": 15,
        "section": "Section 1.5",
        "title": "Monitoring and Penalties for Improper Use",
        "content": """Legitimate Access to Prohibited Material: Requires Line Manager discussion.
Remote Users: Standards apply whether on company or personal equipment.
Monitoring: All resources including computers, email, voicemail belong to Company. Company maintains right to examine any system and inspect data without prior notice.
Penalties for Improper Use: Withdrawal of facilities, disciplinary action up to termination, reporting to police for breaches of law."""
    },
    {
        "page": 16,
        "section": "Section 2",
        "title": "Section 2 - Managing Employee Performance",
        "content": """SECTION - II
MANAGING EMPLOYEE PERFORMANCE
Setting Objectives, Assessing And Managing Employee Performance Including Absence, Misconduct And Capabilities"""
    },
    {
        "page": 17,
        "section": "Section 2.1",
        "title": "Performance Appraisal Policy",
        "content": """Performance Appraisal Policy
Appraisal Policy:
Formal process centred on an annual meeting of each employee and line manager to review achievements and set objectives.

Core Principles of the Appraisal Policy:
- Contributes to a well motivated, competent workforce.
- Two-way communication exercise; sets agreed Personal Development Plan (PDP).
- Supports Training and Development and succession planning.
- Fair and equitable in line with Equality Policy.

Performance Appraisal Implementation:
- Held over designated 4-week period annually.
- Additional 6-month verbal appraisal review encouraged.
- Held in private, strictly confidential.
- Notice given at least 1 week prior."""
    },
    {
        "page": 18,
        "section": "Section 2.2",
        "title": "Controlling Absence Policy",
        "content": """Controlling Absence Policy
Policy:
- Doctor's certificate required for incapacity due to sickness/injury of more than 7 days (including weekends).
- Self-certification form required upon return to work. Qualifying days for statutory pay are Monday to Friday.
- Sickness pay entitlement: If employee complies with notification, paid for up to a maximum period of 12 months.
  - First six months of absence: entitlement to full basic pay.
  - Subsequent six months of absence: entitlement to half of basic salary.
- If employee is unable to perform duties due to sickness/injury for 24 weeks or more in a 12-month period, the company is entitled to terminate employment with written notice of not less than 6 months.
- Sick leave may be paid or unpaid at company discretion."""
    },
    {
        "page": 19,
        "section": "Section 2.3",
        "title": "Leave & Disciplinary Procedure Scope and Suspension",
        "content": """Leave:
All planned leave has to be mutually agreed and approved in advance.
Each employee is entitled to the usual public holidays, together 30 working days in each complete year of the employee's employment. Leave entitlement is calculated from the date employee started work and annual leave counts towards continuous service.
Paid leave will be paid at employee's base pay rate.

Disciplinary Procedure:
Scope: Used only when necessary and as a last resort. Informal counselling preferred prior to disciplinary action.
Suspension: Not a disciplinary action; used pending investigation. Suspended employee receives written confirmation within 3 days stating reason, date/time, timescale, and right of appeal if suspension lasts more than 7 days.
Counselling: Attempt to correct situation and give clear guidelines for improvement."""
    },
    {
        "page": 20,
        "section": "Section 2.3",
        "title": "Disciplinary Warnings: Minor Misconduct vs Gross Misconduct",
        "content": """Examples of Minor Misconduct:
- Persistent lateness and poor time-keeping
- Absence from work without valid reason/authorisation
- Smoking within unauthorised areas
- Failure to work in accordance with prescribed procedures
- Incompetence
- Unreasonable standards of dress or hygiene
- Failure to observe Company regulations

Verbal Warning & First Written Warning.

Examples of Gross - Misconduct (may warrant Final Warning, Demotion or Dismissal):
- Theft, including unauthorised possession of Company property
- Breaches of confidentiality prejudicial to company interest
- Being unfit for duty because of misuse/consumption of drugs or alcohol
- Refusal to carry out management instruction
- Physical assault, breach of peace, verbal abuse
- False declaration of qualifications
- Wilful damage of property
- Incompetence or failure to apply sound professional judgement"""
    },
    {
        "page": 21,
        "section": "Section 2.4",
        "title": "Disciplinary Actions & Capability Procedure",
        "content": """Final Written Warning: For serious offences falling short of dismissal or persisting misconduct.
Downgrading or Transfer: Final attempt to solve problem without dismissal.
Dismissal: For Gross Misconduct or persisting misconduct after exhausting procedures.

Capability Procedure - Introduction:
Fair and objective process to enable managers to ensure performance standards are met.
Includes monitoring performance, establishing criteria, support, and fair procedure if member of staff fails to overcome difficulties."""
    },
    {
        "page": 22,
        "section": "Section 3",
        "title": "Section 3 - Dealing with Employee Concerns",
        "content": """SECTION - III
DEALING WITH EMPLOYEE CONCERNS
Hearing Grievances, Dealing with Bullying & Harassment, and making provisions for 'Whistleblowing'"""
    },
    {
        "page": 23,
        "section": "Section 3.1",
        "title": "Grievance Procedure and Mediation",
        "content": """Grievance Procedure:
Enables staff to formally have a grievance heard.
Stage 1: Raise matter with line manager / supervisor immediately (verbally or in writing).
Stage 2: Appeal against manager's decision.
Stage 3: Final level of appeal to Director responsible for function (or Chief Executive if against a Director).

Using Mediation:
Voluntary process with an independent third-party mediator to help parties in dispute reach agreement. Used for conflict between colleagues, rebuilding relationships, personality clashes, communication issues."""
    },
    {
        "page": 24,
        "section": "Section 3.2",
        "title": "Prevention of Bullying and Harassment at Work",
        "content": """Prevention of Bullying and Harassment at Work:
Statement of Policy:
Zero tolerance policy for bullying or harassment. Applies to all staff, on and off premises, and non-permanent workers.
Harassment Definition:
Any conduct which is unwanted, objectionable, causes humiliation, offence or distress (physical, verbal, or non-verbal)."""
    },
    {
        "page": 25,
        "section": "Section 3.2",
        "title": "Bullying Definition and Investigation Procedure",
        "content": """Bullying Definition:
Repeated and persistent offensive, abusive, intimidating, or insulting behaviour. Includes physical abuse, humiliation in front of colleagues, setting unrealistic targets, cyber bullying.
Complaint procedure:
Discuss informally with line manager or HR; prompt formal investigation if needed. Alleged perpetrator normally moved pending investigation. Strict confidentiality maintained."""
    },
    {
        "page": 26,
        "section": "Section 3.3",
        "title": "Whistleblowing Policy - Scope and Safeguards",
        "content": """Whistleblowing Policy - Making a Disclosure in the Public Interest:
Introduction: High standards of openness, probity and accountability. Allows reporting serious malpractice without fear of reprisal.
Scope of Policy: Covers financial malpractice/fraud, failure to comply with legal obligation, dangers to Health & Safety or environment, criminal activity, improper/unethical conduct.
Safeguards & Protection: Protection offered to employees disclosing in good faith and reasonable belief."""
    },
    {
        "page": 27,
        "section": "Section 3.3",
        "title": "Whistleblowing Confidentiality and Allegations",
        "content": """Confidentiality: Disclosures treated in confidential and sensitive manner.
Anonymous Allegations: Considered at company discretion depending on seriousness and credibility.
Untrue Allegations: Disclosures made in good faith face no action; malicious/vexatious allegations will face disciplinary action."""
    },
    {
        "page": 28,
        "section": "Section 4",
        "title": "Section 4 - Supporting Our Staff in the Workplace",
        "content": """SECTION - IV
SUPPORTING OUR STAFF IN THE WORKPLACE
By ensuring Equality and Fairness in all aspects of Employment; dealing with Alcohol and Drug issues, and ensuring their Health & Safety is properly guarded"""
    },
    {
        "page": 29,
        "section": "Section 4.1",
        "title": "Equality Policy Statement & Commitment",
        "content": """Equality Policy:
Policy Statement: Discrimination and victimisation is unacceptable. Equal treatment regardless of age, disability, gender, marriage, pregnancy/maternity, race, religion, sex, sexual orientation.
Our Commitment: Create inclusive environment, fair promotion/training, annual monitoring and review."""
    },
    {
        "page": 30,
        "section": "Section 4.1",
        "title": "Rights of Disabled People, Training & Termination Notice",
        "content": """Rights of Disabled People:
Reasonable adjustments, inclusion in training programmes, fair hiring considerations.
Training and Development: Internal and external training to ensure safe and competent work.
Notice of Termination: Either party may terminate employment by one calendar month's prior written notice (or payment in lieu of basic salary). Immediate termination for gross breach/dishonesty."""
    },
    {
        "page": 31,
        "section": "Section 4.2 & 4.3",
        "title": "Drug & Alcohol Policy & Health & Safety Policy",
        "content": """Drug and Alcohol Abuse Policy:
Zero tolerance policy for illicit drugs on premises or attending work under influence of drugs/alcohol. Contravening may lead to instant dismissal.

Health and Safety Policy:
Complies with Health & Safety at Work legislation. First Aid provision provided. Condemnation and disposal of equipment checked by Safety Officer."""
    },
    {
        "page": 32,
        "section": "Section 4.3",
        "title": "Workplace Safety: Lifting, Non-Smoking, VDUs, Hours",
        "content": """Lifting and Handling: Safe lifting techniques.
Non-Smoking on Company Premises: No smoking in buildings.
Control of Substances Hazardous to Health (COSHH).
VDUs: Screen equipment regulations and sight screening.
Control of Working Time: Office hours 9:30 am to 5:30 pm Monday to Friday with 1 hour lunch break. Maximum 48 hours per week including overtime."""
    },
    {
        "page": 33,
        "section": "Section 4.3",
        "title": "Contractors and Safety",
        "content": """Contractors: Obligation to ensure equipment and premises under control are safe. Must observe Fire Safety Procedures. Say NO to Drugs campaign."""
    },
    {
        "page": 34,
        "section": "Company Rules",
        "title": "Staff Handbook & Company Property & Outside Employment",
        "content": """Company Rules & Regulations:
Staff Handbook: Informational compilation of policies, at-will employment clauses, supersedes prior versions.
Company Property: Responsible use of computers, phones, internet, email; no use for personal benefit.
Outside Employment: Employees are strictly not permitted to engage in outside work or to hold other jobs."""
    },
    {
        "page": 35,
        "section": "Company Rules",
        "title": "IT Security, Personal Mail, Calls & Smoking Policy",
        "content": """IT Security, Personal Mail & Calls Policy:
Company technology belongs to Enso Group; routinely monitored. No defamatory, discriminatory, or pornographic use.
Smoking in the Office: Prohibited in all areas of company buildings, vehicles, and company-sponsored off-site events. Permitted in parking lots subject to security in-charge permission."""
    },
    {
        "page": 36,
        "section": "Company Rules",
        "title": "Non-Disclosure of Confidential Information & Security",
        "content": """Non-Disclosure of Confidential Information:
Employees required to sign Non-Disclosure Agreement (NDA). Confidential data includes compensation data, financial information, proposals. Conversations should not be conducted in elevators, restaurants, cellular phones.
Office Security & Emergency Evacuation: Familiarity with emergency plans, completion of accident and incident reports."""
    },
    {
        "page": 37,
        "section": "Company Rules",
        "title": "Conflict of Interest & Acceptance of Advantage",
        "content": """Conflict Of Interest:
Duty to act in company's best interest. Disclose potential conflicts: consulting to competitors, hiring family members, board membership, accepting gifts or discounts.
Acceptance of Advantage:
In compliance with Prevention of Bribery Ordinance. Decline advantages that affect objectivity. Entertainment permitted if not lavish or frequent."""
    },
    {
        "page": 38,
        "section": "Company Rules",
        "title": "Theft Attempted & Asset Security Guidelines",
        "content": """Theft Attempted:
Dishonestly appropriating property. Assets (such as laptops) must be kept under lock and key when not in use. In transit, asset must be in physical possession of executive. Damage/theft due to negligence requires executive to replace laptop or compensate actual cost."""
    },
    {
        "page": 39,
        "section": "Annexure - I",
        "title": "Annexure - I Title Page",
        "content": """ANNEXURE - I
On Boarding, Probation, Training & Development, Relocation, and Off Boarding Policies"""
    },
    {
        "page": 40,
        "section": "Annexure - I",
        "title": "[A] On Boarding Process",
        "content": """[A] On Boarding Process
Meaning/Purpose: Integrating new employees, adjusting to culture, establishing goals and priorities.
Scope & Eligibility: Applies to all newly joined employees on the roll of Enso Group.
Policy Features:
1. Joining Formalities: Collecting documents, login ID creation, KRA setting, PF/bank forms.
2. Induction Program: Organisation introduction (history, vision, mission, org chart), Role expectations, work culture, growth plan.
3. Buddy Up Program (optional): Assigning a peer buddy to answer questions and guide newcomer."""
    },
    {
        "page": 41,
        "section": "Annexure - I",
        "title": "[A] On Boarding Remarks and Objectives",
        "content": """Remarks:
Common objectives of onboarding program: build employee identification, positive attitude, socialize, avoid misunderstandings, relieve anxiety, shorten learning curve."""
    },
    {
        "page": 42,
        "section": "Annexure - I",
        "title": "[B] Probation Policy",
        "content": """[B] Probation Policy
Meaning/Purpose:
The probationary period is a time for you to learn about your job and become familiar with the Working culture of Enso Group. During this time, your supervisor will explain your department's policies and procedure, job duties, and performance expectations.

Scope & Eligibility:
• All employees up to Sr. Manager would be placed in Probation for a period of 3 months from the date of their joining.
• All employees above Sr. Manager will be treated as confirmed employees from the date of joining.
• At the end of the probation period the employee will be considered for confirmation based on the Review Report of the Superior and the respective Departmental Head.

Policy Features:
Two weeks before end of probation, Probation Review Report (PRR) sent to department head.
Three recommendations:
1. Appointment confirmed as per Appointment Letter.
2. Appointment extended further for specified number of months.
3. Appointment terminated.

Extension of Probation:
- Extended in weak cases at sole discretion of Management.
- Can be extended only at original probation period.
- Only one extension can be recommended and cannot exceed duration of original probationary period (max 3 months).

Termination of Employment: HR reviews if employee was given all resources and supervision."""
    },
    {
        "page": 43,
        "section": "Annexure - I",
        "title": "[B] Probation Policy - Monitored Factors",
        "content": """Remarks:
During the Probationary Period, the following factors will be closely monitored:
- Knowledge, Skills and Deliverables
- Attitude towards work and organisation
- Behaviour with Superiors and Peers
- Ability to adjust to requirements of the job
- Adherence to organisation culture values and discipline"""
    },
    {
        "page": 44,
        "section": "Annexure - I",
        "title": "[C] Training and Development",
        "content": """[C] Training and Development
Meaning/Purpose: Effective training benefits individual and organization.
Scope & Eligibility: Applies to all staff members of Enso Group.
Policy Features: Grooming norms, behavioural dos & don'ts, technical training by technical team to meet desired competencies."""
    },
    {
        "page": 45,
        "section": "Annexure - I",
        "title": "[D] Relocation Policy",
        "content": """[D] Relocation Policy
Meaning/Purpose: Reimbursement of defined expenses when salaried employee is permanently transferred at Company request.
Scope & Eligibility: Applies to all employees on payroll excluding Top Management, transferred for no less than 12 months to a location at least 50 miles farther from residence.
Policy Features: Reimbursement of vouchers submitted to HR, approved by supervising manager, Functional Head, and HR."""
    },
    {
        "page": 46,
        "section": "Annexure - I",
        "title": "[E] Off-Boarding Process: Resignation, Termination, Absconding",
        "content": """[E] Off-Boarding Process
Resignation: Written notice through Dept Head to HR. Required 30 days notice period; failure to serve 30 days may forfeit pay equivalent to notice period.
Termination: Involuntary termination of services with salary in lieu of notice if applicable.
Absconding on Duty (AOD): Absent from duty without permission for 3 consecutive days or more deemed abandoned employment."""
    },
    {
        "page": 47,
        "section": "Annexure - I",
        "title": "[E] Full & Final Settlement (F&F)",
        "content": """Full & Final Settlement (F&F):
Policy:
- Made only after recovering Company property and dues.
- Final settlement within ONE WEEK from date of Termination if no dues/recovery.
- Prepared in duplicate.
- Payment made from Head Office only by A/C Payee Cheque and not by Cash.
- Basic pay considered for calculating notice pay."""
    },
    {
        "page": 48,
        "section": "Annexure - II",
        "title": "Annexure - II Title Page",
        "content": """ANNEXURE - II
Employee of the year to be declared on 31st December of every year. Recognition trophy to be provided along with one months bonus salary."""
    },
    {
        "page": 49,
        "section": "Annexure - II",
        "title": "[A] Equal Opportunities Policy",
        "content": """[A] Equal Opportunities
Meaning/Purpose: Fair chance to obtain employment and gain Promotion according to abilities and qualifications. Merit principle.
Scope & Eligibility: All employees and potential employees.
Policy Features: Equal Employment Opportunity (EEO) free from discrimination based on sex, race, colour, age, disability, sexual orientation, religion, etc."""
    },
    {
        "page": 50,
        "section": "Annexure - II",
        "title": "[A] Equal Opportunities - Direct and Indirect Discrimination",
        "content": """Remarks:
Failure to comply leads to disciplinary action.
Discrimination may be direct or indirect. Indirect discrimination occurs when an unreasonable neutral requirement disproportionately disadvantages a protected group."""
    },
    {
        "page": 51,
        "section": "Annexure - II",
        "title": "[B] Data card / Visiting Cards / Emails Policy",
        "content": """[B] Data card/Visiting Cards/Emails Policy
Scope & Eligibility:
- Employees in Management level AVP & above will be eligible for benefit.
- Extensive official travel within India required.
- Approval by Business Head and HR Business Partner.
Policy Features: Only official service providers used; excess usage requires approvals; Company property must be returned upon exit; strictly for official usage."""
    },
    {
        "page": 52,
        "section": "Annexure - III",
        "title": "Annexure - III Title Page",
        "content": """ANNEXURE - III
Salary - 1st of every month
Holiday List - 1st Jan of every year"""
    },
    {
        "page": 53,
        "section": "Annexure - III",
        "title": "[A] Dress Code Policy",
        "content": """[A] Dress Code
Meaning/Purpose: Professional cleanliness and business image. At no point must employees resort to casual wear during business hours.
Policy Features:
- Men: Uniform if provided, black shoes; or Full/half sleeve shirt, trousers & black/brown shoes; ties and suits encouraged.
- Women: Sarees / Salwar Kameez / Slacks / Shirts, trousers / Formals.
- Inappropriate: Tight fitting pants, sports wear, mini skirts, round neck t-shirts, slippers/chappals, denims.
- Casual: Smart Business casual allowed on weekends and bank holidays only (denims and V-neck t-shirts permitted then)."""
    },
    {
        "page": 54,
        "section": "Annexure - III",
        "title": "[B] Work Timing Policy",
        "content": """[B] Work timing Policy
Scope & Eligibility: All employees and contractual staff on roll. Encouraged to reach 10 mins prior.
Policy Features:
- Corporate Office: Office Time 9:30am to 5:30pm | Weeks Off: Saturday & Sunday | Lunch time: 1:00pm - 1:45pm.
Remarks:
- Corporate office staff have option of flexi timing (report 1 hour early or late) maintaining 8 hours shift, subject to manager approval."""
    },
    {
        "page": 55,
        "section": "Annexure - III",
        "title": "[C] Punctuality and Attendance Policy",
        "content": """[C] Punctuality and Attendance
Meaning/Purpose: Regular attendance is essential for optimal productivity and customer service.
Scope & Eligibility: All employees and contractual staff.
Policy Features:
- Scheduled Absences: 24-hour advance notice and manager approval.
- Unscheduled Absences: Must call supervisor within 1 hour after scheduled start time (failure may result in Loss of Pay).
- All Enso employees have a 30 day leave grant inclusive of all eventualities.
- Punctuality: Report 10 mins prior; working hours 9:30am to 5:30pm."""
    },
    {
        "page": 56,
        "section": "Annexure - III",
        "title": "[C] Attendance Remarks & Leave Limits",
        "content": """Remarks:
- 30 days off in a year includes sick and emergency leaves and excludes designated holidays and weekends.
- Holiday list declared on 1st Jan of every calendar year.
- Any leave exceeding 30 days shall incur pending reflecting in salary cuts."""
    },
    {
        "page": 57,
        "section": "Annexure - III",
        "title": "[D] Compensation Policy",
        "content": """[D] Compensation Policy
Salary components:
Basic, Home rent allowance (HRA), Leave traveling allowance (LTA), Medical Reimbursement, Conveyance, Project Development Allowance, Food coupons, Employer Contribution to PF, ESIC and Performance Bonus shall form a part of the CTC.

Disbursement:
Employees shall be paid salary on a monthly basis based on attendance by 31st of every month (or preceding working day if 31st is Saturday/Sunday/Holiday)."""
    },
    {
        "page": 58,
        "section": "Annexure - III",
        "title": "[E] Staff Advances Policy",
        "content": """[E] Staff Advances
Policy:
- Provided for emergency exigencies for permanent employees with 1 year or more service, with HOD approval.
- Salary for month in part or full given as advance. Apply 15 days in advance.
- Interest free. Repayment in 6 equal monthly instalments deducted from salary.
- Availed only once a year."""
    },
    {
        "page": 59,
        "section": "Annexure - III",
        "title": "[F] Employment of Relatives Policy",
        "content": """[F] Employment Of Relatives Policy
Meaning/Purpose: Welcomes relative applications based on qualification for openings not under direct or indirect supervision of relative.
Scope & Eligibility: Relatives cannot work directly for or supervise a relative. If relationship established post employment, decision within 30 days on transfer."""
    },
    {
        "page": 60,
        "section": "Annexure - III",
        "title": "[G] Leave Policy - Scope & Privilege Leave (PL)",
        "content": """[G] Leave Policy
Meaning/Purpose:
This policy encourages employees to take a break from work to maintain a healthy, stress-free and productive staff. Sets out leave types and procedures.

Scope & Eligibility:
• Leave year is as per the calendar year (1st January – 31st December).
• The different types of leaves covered under this policy are:
  - Privilege Leave (PL) – 12 days
  - Casual Leave (CL) – 6 days
  - Sick Leave (SL) – 6 days
  - Stress Leave (STL) – 6 days
  - Maternity Leave (leeway)
• The policy is applicable for all permanent employees of ENSO GROUP and not for Contract employees. (For contract employees, leave is per individual contract).
• During probation no leave will be credited to employees.
• All leaves should be approved by the manager on mail.

Policy Features:
Leave Type: Privilege Leave (PL)
- Eligibility: All permanent employees are eligible to avail PL. PL is calculated for a period of one calendar year (1st Jan-31st Dec).
- Entitlement: 12 days PL is allowed to each employee. Unavailed PL cannot be carry-forward to next calendar year.
- Encashment: An employee can accumulate and avail his PL at a stretch within a calendar year. Accumulated leave balance can be en-cashed only as a part of full & final settlement at the basic pay.
- Procedure: All employees are required to apply for PL on mail to their manager at least a week in advance for approval. Leave taken without manager's approval will be considered as Unapproved leave leads to salary deduction."""
    },
    {
        "page": 61,
        "section": "Annexure - III",
        "title": "[G] Leave Policy - Casual Leave, Sick Leave, Stress Leave",
        "content": """[G] Leave Policy (Continued)
Casual Leave (CL):
- Eligibility: All permanent employees eligible. Calculated per calendar year (1st Jan - 31st Dec).
- Entitlement: 6 days CL allowed to each employee. Unavailed CL cannot be carry-forward.
- Encashment: Cannot be accumulated, encashed or carried forward.
- Procedure: Apply on mail at least 1 week in advance.

Sick Leave (SL):
- Eligibility: All permanent employees eligible. Calculated per calendar year.
- Entitlement: 6 days SL allowed. Used for medical/dental/optical treatment or physical illness/injury.
- Encashment: Cannot be accumulated, encashed or carried forward.
- Procedure: Inform reporting manager via Telephone, Email or SMS.

Stress Leave (STL):
- Eligibility: All permanent employees eligible. Calculated per calendar year.
- Entitlement: 6 days SL allowed.
- Procedure: Apply 1 day in advance. Cannot be accumulated, encashed or carried forward."""
    },
    {
        "page": 62,
        "section": "Annexure - III",
        "title": "[G] Leave Policy - Maternity Leave (Leeway)",
        "content": """[G] Leave Policy - Maternity Leave (Leeway)
Leave Type: Maternity Leave (Leeway)
- Eligibility: ML shall be available to all confirmed female staff in accordance with the law applicable from time to time. Female staff, who have worked for at least 80 days in preceding 12 months, are entitled to ML.
- Entitlement: In case of miscarriage or medical termination of pregnancy, four weeks leave with pay from the date of miscarriage is permitted by producing satisfactory evidence.
- Encashment / Provision: The company will provide a total of 12 weeks (- 90days) as ML with pay, of which not more than 6 weeks (- 45days) should precede the expected date of delivery.
- Extension of leave beyond regular ML will be adjusted against accumulated leave balance, or treated as leave without pay. Subject to approval of concerned reporting authority.
- Procedure: The employee must apply for ML at least one month before taking leave. Must submit Certificate of fitness from Doctor upon returning.

Remarks:
- Must not affect delivery deadlines.
- Approved by reporting officer; for Maternity Leave the HOD shall be the competent authority to approve.
- Maximum 30 days off work premises in total; salary deducted upon exceeding 30 days (excluding statutory leaves)."""
    },
    {
        "page": 63,
        "section": "Annexure - III",
        "title": "[H] Reward & Recognition Policy",
        "content": """[H] Reward & Recognition
Meaning/Purpose: Reduce attrition, recognize critical performance.
Scope & Eligibility: All employees, departments, functions.
Policy Features:
- EOY - Employee of the Year: Decided by senior management and peer recommendation.
- Reward: Cash Rewards (One month salary bonus) and Trophy memorabilia.
- Also includes EOM (Employee of the Month) and EOQ (Employee of the Quarter)."""
    },
    {
        "page": 64,
        "section": "Annexure - III",
        "title": "[I] Anti Sexual Harassment Policy",
        "content": """[I] Whistle Blower Policy & Anti Sexual Harassment Policy
Anti Sexual Harassment Policy:
Strict zero tolerance for sexual harassment.
Definitions include unwelcome sexual advances, requests for sexual favours, sexual remarks, leering, gestures.
Complaint Procedure:
Written complaint signed to HRD. Handled with utmost confidentiality by Committee comprising Director, CFO, Company Secretary & Legal Counsel, and Head HR."""
    },
    {
        "page": 65,
        "section": "Annexure - III",
        "title": "Whistle Blower Policy Details",
        "content": """Whistle Blower Policy:
Meaning/Purpose: Enables reporting violations of policies, laws, bribery, fraud, mismanagement, data manipulation without fear of retaliation.
Role of Whistle Blower: Reporting party with reliable information; not required to act as investigator."""
    },
    {
        "page": 66,
        "section": "Annexure - IV",
        "title": "Annexure - IV Title Page",
        "content": """ANNEXURE - IV
Traveling Policies
Long distance travel policy and Short distance travel policy"""
    },
    {
        "page": 67,
        "section": "Annexure - IV",
        "title": "[A] Long Distance Travel Policy",
        "content": """[A] Long Distance Travel Policy
Scope & Eligibility: Permanent employees on rolls; not applicable to contractual staff.
Guidelines:
- Explore videoconferencing first.
- Travel advance provided for business only.
- Travel Requisition Number mandatory.
- Max 2 international trainings per employee per calendar year.
Sanction Authority: International travel authorized by Respective Approving Authority, For Directors by Board."""
    },
    {
        "page": 68,
        "section": "Annexure - IV",
        "title": "Ticketing & Air Travel Booking Class",
        "content": """Travel Arrangements & Ticketing:
- Bookings done by Travel Desk. International tickets booked 15 days in advance.
- Self booking allowed if 5% cheaper than quote given by travel desk.

Air Travel Booking Class:
- All Travelers, All Travel: Economy Class.
- Directors / Sr. Management: >4 hours: Business / Economy; <4 hours: Economy / Business.
- Roaming telephone: Roaming SIM cards, WiFi usage."""
    },
    {
        "page": 69,
        "section": "Annexure - IV",
        "title": "Per Diem Reimbursement (International Travel)",
        "content": """(A.) PER DIEM REIMBURSEMENT (International Business Travel)
Covers meals, laundry, and transportation expenses.
Limits:
- Up to Sr. Management: US $75 PER DAY
- Above Sr. Management level: US $100 PER DAY
- In case company incurs boarding arrangements: US $40 per day allowance for other expenses."""
    },
    {
        "page": 70,
        "section": "Annexure - IV",
        "title": "Accommodation & Personal Phone Calls (International)",
        "content": """(B.) ACCOMMODATION (International)
Hotel Pay Day Limits:
- Up to Sr. Management: Within Asia (Except Japan)/Australia: US $250; US/Europe/Japan: US $300.
- Above Sr. Management: Within Asia (Except Japan)/Australia: US $300; US/Europe/Japan: US $350.
- Stay with friends/family allowance: US $75 to US $125.

(C.) PERSONAL PHONE CALLS:
Max 20 minutes personal calls per week (5-day week). No calls from air/rail/cellular car phones."""
    },
    {
        "page": 71,
        "section": "Annexure - IV",
        "title": "Business Entertainment & Personal / Leisure Travel",
        "content": """Official Calls & Non-Reimbursable Expenses:
Non-reimbursable: Health club, gift shop, mini bar, toiletries, reward programme fees.
(D.) Business Entertainment Expenses: Approved by Functional Head; group meals paid by highest ranking employee.
(E.) Personal/Leisure Travel: Cannot combine with business travel unless no additional cost to company and pre-approved."""
    },
    {
        "page": 72,
        "section": "Annexure - IV",
        "title": "International Travel Claim Process",
        "content": """(F.) CLAIM PROCESS (International Travel):
- Settle claims with Finance within 7 working days of return. Unsettled claims recovered through payroll. Claims not settled in 30 days are auto-settled.
- Boarding pass is mandatory document.
- Reimbursement via bank fund transfer only (no cheques).
- Rates reviewed every 3 years."""
    },
    {
        "page": 73,
        "section": "Annexure - IV",
        "title": "[B] Short Distance Travel Policy",
        "content": """[B] Short Distance Travel Policy
Scope & Eligibility: Permanent employees on rolls; not applicable to contractual staff.
Guidelines: Travel Advance given, Travel Requisition form mandatory, disciplinary action for fraudulent claims."""
    },
    {
        "page": 74,
        "section": "Annexure - IV",
        "title": "Short Distance Travel Booking & Ticketing",
        "content": """Sanctioning Authority: Requisition form approved by reporting manager and counter approved by Skip Level Manager.
Ticketing: Domestic ticket booking reasonably in advance. Self-booking allowed if 5% cheaper. Shortlist 3 preferred carriers."""
    },
    {
        "page": 75,
        "section": "Annexure - IV",
        "title": "Domestic Travel Per Diem, Entitlements & Accommodation",
        "content": """Domestic Travel Policy Features:
A. Per Diem Allowance: Company bears travel, accommodation, laundry, food, conveyance (excluding alcoholic beverages and tobacco).
B. Travel Entitlements:
- Leadership Level (Chairman, MD, Directors): 1st class rail / Private AC Cab / Air Economy or Air Business Class (at discretion).
- All other levels: Economy class ticket at lowest available fare.
- Private taxi allowed for interstate travel where metered taxi not available.
C. Accommodation: Company transit accommodation or tied-up hotels."""
    },
    {
        "page": 76,
        "section": "Annexure - IV",
        "title": "Domestic Accommodation Rules & Non-Reimbursable Items",
        "content": """Hotel Accommodation & Rules:
- First preference to company transit accommodation, then tie-up hotels. Self-booking if 5% cheaper.
- Laundry only after 3 days continuous travel.
- Non-reimbursable: Health club, mini bar, toiletries.
- Stay with friends/family permitted.
- Group meals paid by highest ranking employee."""
    },
    {
        "page": 77,
        "section": "Annexure - IV",
        "title": "Domestic Leisure Travel & Claim Process",
        "content": """Personal/Leisure Travel: Cannot combine with business travel unless pre-approved and no additional cost.
Claim Process:
- Travel Settlement Form approved by Reporting Manager & Skip Level Manager.
- Forward details within 7 working days of return with boarding pass / tickets."""
    },
    {
        "page": 78,
        "section": "Annexure - IV",
        "title": "Domestic Travel Settlement & Reimbursement",
        "content": """Domestic Claim Settlement:
- Proof of travel mandatory (boarding pass, train ticket).
- Claims without bills require Director approval (for Directors: Board approval).
- Reimbursement via bank fund transfer.
- During exit: processed with full & final settlement only."""
    },
    {
        "page": 79,
        "section": "Back Cover",
        "title": "Enso Group - Enlightened Life",
        "content": """Enlightened Life
ENSO GROUP HR POLICY MANUAL
End of Document."""
    }
]

def main():
    # Write JSON
    json_path = DATA_DIR / "hr_manual_extracted.json"
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(PAGES_DATA, f, indent=2, ensure_ascii=False)
    print(f"Extracted data written to {json_path} ({len(PAGES_DATA)} pages)")

    # Create real PDF file data/hr_manual.pdf using pure python binary structure
    pdf_path = DATA_DIR / "hr_manual.pdf"
    create_binary_pdf(pdf_path, PAGES_DATA)
    print(f"PDF document created at {pdf_path}")

def create_binary_pdf(target_path, pages):
    """Generates a valid standard PDF document from pages data"""
    try:
        from pypdf import PdfWriter
        # If pypdf is available, we can also use canvas or simple text pages
    except Exception:
        pass
    
    # Let's write a standard clean multi-page PDF generator in Python
    # A standard PDF file has: %PDF-1.4 header, Objects (Catalog, Outlines, Pages, Page, Font, Contents), Xref, Trailer
    objects = []
    
    def add_object(content_str):
        obj_num = len(objects) + 1
        objects.append(content_str)
        return obj_num
    
    # 1: Font
    font_obj = add_object("<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica >>")
    font_bold_obj = add_object("<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica-Bold >>")
    
    page_obj_nums = []
    
    # For each page, create content stream and page object
    # We will populate them in a second pass
    for i, p in enumerate(pages, 1):
        text = f"ENSO GROUP HR POLICY MANUAL - PAGE {p['page']}\n\n[{p['section']}] {p['title']}\n\n" + p['content']
        # Escape parenthesis in text stream
        clean_lines = []
        for line in text.split("\n"):
            sanitized = line.replace("\\", "\\\\").replace("(", "\\(").replace(")", "\\)")
            clean_lines.append(sanitized)
            
        stream_lines = ["BT", "/F2 14 Tf", "40 760 Td", f"({clean_lines[0]}) Tj", "0 -22 Td", "/F2 11 Tf", f"({clean_lines[1] if len(clean_lines) > 1 else ''}) Tj", "/F1 9 Tf"]
        y_step = -13
        current_y = 716
        for line in clean_lines[2:]:
            if not line.strip():
                stream_lines.append("0 -10 Td")
                current_y -= 10
            else:
                # Wrap line if long
                chunks = [line[k:k+80] for k in range(0, len(line), 80)]
                for c in chunks:
                    stream_lines.append("0 -13 Td")
                    stream_lines.append(f"({c}) Tj")
                    current_y -= 13
                    if current_y < 50:
                        break
            if current_y < 50:
                break
        stream_lines.append("ET")
        stream_content = "\n".join(stream_lines)
        stream_len = len(stream_content.encode("latin-1", "replace"))
        
        content_obj = add_object(f"<< /Length {stream_len} >>\nstream\n{stream_content}\nendstream")
        page_obj = add_object(f"<< /Type /Page /Parent 3 0 R /MediaBox [0 0 595 842] /Resources << /Font << /F1 1 0 R /F2 2 0 R >> >> /Contents {content_obj} 0 R >>")
        page_obj_nums.append(page_obj)
        
    # Pages root object (Object 3)
    kids_str = " ".join([f"{num} 0 R" for num in page_obj_nums])
    pages_root_content = f"<< /Type /Pages /Kids [ {kids_str} ] /Count {len(page_obj_nums)} >>"
    
    # We need to insert pages_root at index 2 (Object 3)
    # Let's rebuild properly:
    # Obj 1: Font
    # Obj 2: Font-Bold
    # Obj 3: Pages Root
    # Obj 4..N: Content streams & Page objects
    # Obj Last: Catalog
    
    # Let's reconstruct cleanly:
    final_objs = []
    final_objs.append("<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica >>") # 1
    final_objs.append("<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica-Bold >>") # 2
    final_objs.append("") # 3 placeholder for Pages
    
    final_page_refs = []
    curr_idx = 4
    for p in pages:
        text = f"ENSO GROUP HR POLICY MANUAL - PAGE {p['page']}\n[{p['section']}] {p['title']}\n" + p['content']
        clean_lines = []
        for line in text.split("\n"):
            sanitized = line.replace("\\", "\\\\").replace("(", "\\(").replace(")", "\\)")
            clean_lines.append(sanitized)
            
        stream_lines = ["BT", "/F2 13 Tf", "40 780 Td", f"({clean_lines[0]}) Tj", "/F2 10 Tf", "0 -18 Td", f"({clean_lines[1]}) Tj", "/F1 8 Tf"]
        current_y = 740
        for line in clean_lines[2:]:
            if not line.strip():
                stream_lines.append("0 -8 Td")
                current_y -= 8
            else:
                chunks = [line[k:k+85] for k in range(0, len(line), 85)]
                for c in chunks:
                    stream_lines.append("0 -11 Td")
                    stream_lines.append(f"({c}) Tj")
                    current_y -= 11
                    if current_y < 45:
                        break
            if current_y < 45:
                break
        stream_lines.append("ET")
        stream_content = "\n".join(stream_lines)
        stream_len = len(stream_content.encode("latin-1", "replace"))
        
        c_obj_idx = curr_idx
        p_obj_idx = curr_idx + 1
        curr_idx += 2
        
        final_objs.append(f"<< /Length {stream_len} >>\nstream\n{stream_content}\nendstream")
        final_objs.append(f"<< /Type /Page /Parent 3 0 R /MediaBox [0 0 595 842] /Resources << /Font << /F1 1 0 R /F2 2 0 R >> >> /Contents {c_obj_idx} 0 R >>")
        final_page_refs.append(f"{p_obj_idx} 0 R")
        
    catalog_idx = curr_idx
    final_objs[2] = f"<< /Type /Pages /Kids [ {' '.join(final_page_refs)} ] /Count {len(final_page_refs)} >>"
    final_objs.append(f"<< /Type /Catalog /Pages 3 0 R >>")
    
    # Build complete PDF bytes
    pdf_bytes = bytearray(b"%PDF-1.4\n%\xe2\xe3\xcf\xd3\n")
    offsets = []
    
    for i, obj_content in enumerate(final_objs, 1):
        offsets.append(len(pdf_bytes))
        obj_str = f"{i} 0 obj\n{obj_content}\nendobj\n"
        pdf_bytes.extend(obj_str.encode("latin-1", "replace"))
        
    xref_offset = len(pdf_bytes)
    pdf_bytes.extend(f"xref\n0 {len(final_objs) + 1}\n0000000000 65535 f \n".encode("latin-1"))
    for off in offsets:
        pdf_bytes.extend(f"{off:010d} 00000 n \n".encode("latin-1"))
        
    trailer_str = f"trailer\n<< /Size {len(final_objs) + 1} /Root {catalog_idx} 0 R >>\nstartxref\n{xref_offset}\n%%EOF\n"
    pdf_bytes.extend(trailer_str.encode("latin-1"))
    
    with open(target_path, "wb") as f:
        f.write(pdf_bytes)

if __name__ == "__main__":
    main()
