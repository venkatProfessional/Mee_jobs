from pages.add_user import AddUser

if __name__ == "__main__":
    # login test
    # page = DashboardPage()
    # page.verify_dashboard()

    # add user functionality
    adduser = AddUser()
    adduser.automate_add_user_page_navigation()
    adduser.export_from_excel_and_add_users()


