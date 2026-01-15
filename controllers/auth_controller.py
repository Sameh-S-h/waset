from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from repositories.repository_factory import RepositoryFactory

auth_bp = Blueprint('auth', __name__, url_prefix='/auth')

@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        role = request.form.get('role')
        
        phone = request.form.get('phone')
        address = request.form.get('address')
        shipping_company = request.form.get('shipping_company')
        industry_type = request.form.get('industry_type')

        user_repo = RepositoryFactory.get_repository("user")
        
        if user_repo.get_by_email(email):
            flash("Email already exists!", "danger")
            return redirect(url_for('auth.register'))

        user_repo.add_user(username, email, password, role, phone, address, shipping_company, industry_type)
        flash("Registration successful! Please login.", "success")
        return redirect(url_for('auth.login'))

    return render_template('auth/register.html')

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user_repo = RepositoryFactory.get_repository("user")
        user = user_repo.get_by_email(email)

        if user and user.password_hash == password:
            session['user_id'] = user.id
            session['username'] = user.username
            session['role'] = user.role
            flash(f"Welcome, {user.username}!", "success")
            return redirect(url_for('home'))
        else:
            flash("Invalid email or password", "danger")

    return render_template('auth/login.html')

@auth_bp.route('/logout')
def logout():
    session.clear()
    flash("You have been logged out.", "info")
    return redirect(url_for('auth.login'))