**Project: EduTrack**

**Description:**
EduTrack is an educational institute management system designed to streamline data access for both students and lecturers. By connecting the database to a Language Model (LLM), it facilitates easy retrieval of student information and lecturer notes. 

**Use Cases:**

1. **Student Information:**
   - **Attributes:** StudentID, Name, Age, Branch, Address, FeesPaid, FeesRemaining, TotalFees
   - **Functionality:** This feature enables users to access comprehensive student details including personal information, financial status, and academic records.

2. **Lecturer Notes:**
   - **Attributes:** Subject Name, Subject Code, Drive Link
   - **Functionality:** Lecturers can easily retrieve notes they've prepared for a particular subject by searching using either the subject name or code. The system returns the corresponding Drive link for quick access to the notes.

**Installation:**
1. Ensure you have Python installed.
2. Clone the repository: `git clone https://github.com/abrarsharif66/test_hackprix`
3. Navigate to the project directory: `cd test_hackprix`
4. Install dependencies: `pip install -r requirements.txt`

**Running the Application:**
- To start the Streamlit app for student data, run: `streamlit run Student_data.py`

**Directory Structure:**
- **Student_data.py:** Streamlit app for accessing student information.
- **Lecturer_notes.py:** Streamlit app for accessing lecturer notes.
- **requirements.txt:** File containing the required Python packages.

**Note:** Ensure proper configuration of database connection details for seamless operation of the application.

**Deployment:**
We have deployed EduTrack on AWS EC2. To access it, visit [EduTrack on AWS EC2](http://your_ec2_instance_ip:8501) in your browser.

**Contributors:**
- Abrar Sharif
- Mohammed Abdul Junaid


**Feedback and Contributions:**
We welcome any feedback or contributions to enhance the functionality and usability of EduTrack. Please feel free to submit your suggestions or pull requests to the repository.
