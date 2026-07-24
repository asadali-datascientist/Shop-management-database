
import streamlit  as st 

def about():
    st.set_page_config(page_title="About",
                       layout="wide")
    
    
    st.title("🛍️ About Shop Management System")
    st.write("""
             Welcome to the Shop Management System, 
             a modern desktop application developed to simplify 
             and automate daily shop operations. 
             This system provides an efficient way to manage products, 
             inventory, employees, sales,and stocks 
            from one centralized platform.
             """)
    st.divider()
    st.title("🎯 Our Mission")
    st.write('''
             Our mission is to help shop owners replace manual 
             record-keeping with a fast, secure, and reliable digital solution. 
             By automating routine tasks, the system saves time, reduces errors, 
             and improves overall business management.
             ''')
    st.divider()
    st.title("✨ Key Features")
    st.write('''
             🔐 Secure Login & Registration
             
                📦 Product Management
                
                📊 Stock Management
                
                👥 Customer Management
                
                👨‍💼 Employee Management
                
                💰 Sales Management
                
                📈 Sales History
                
                🔍 Product Search
                
                👤 Multi-User Support
                
                🗄️ MySQL Database Integration
                
             ''')
    st.divider()
    st.title("⚙️ Technologies Used")
    st.write('''
             Python
             
            Streamlit
            
            MySQL
            
            Pandas
            
            SQL
             ''')
    st.title("🚀 Why Choose This System?")
    st.write('''
             Simple and easy-to-use interface
             
                Fast product and customer management
                
                Real-time stock monitoring
                
                Secure user authentication
                
                Automatic sales recording
                
                Organized database management
                
                Multi-user support
                
                Reliable and efficient performance
            ''')
    st.divider()
    st.title("📌 Project Information")

    st.write('''
             Project Name: Shop Management System

                Version: 1.0

                Application Type: Desktop Web Application

                Database: MySQL

                Framework: Streamlit
            ''')
    st.divider()
    st.title("👨‍💻 Developed By")
    st.write('''
             Developer: Asad Ali

            This project was developed as a learning and 
            practical implementation
            of Python, Streamlit, 
            and MySQL to build a 
            complete Shop Management System.
            ''')
    st.subheader("Email: asadali471643@gmail.com")
    st.divider()
    st.title("📞 Contact")
    st.write('''For suggestions, improvements, or technical support, 
                 please contact the developer.''')
    st.divider()
    st.title("⭐ Thank You")
    st.write('''Thank you for using the Shop Management System. 
             We hope this application helps you manage your business more 
             efficiently, accurately, and professionally.''')