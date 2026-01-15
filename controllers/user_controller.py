from flask import Blueprint, render_template, session, redirect, url_for, request, flash
from repositories.repository_factory import RepositoryFactory

user_bp = Blueprint('user', __name__, url_prefix='/user')

@user_bp.route('/profile')
def profile():
    # 1. لو مفيش يوزر في الجلسة، حوله للوجين
    if 'user_id' not in session:
        return redirect(url_for('auth.login'))

    user_repo = RepositoryFactory.get_repository("user")
    user = user_repo.get_by_id(session['user_id'])

    # 2. (التصحيح هنا) لو اليوزر اتمسح من الداتا بيز، نعمل خروج فوراً
    if user is None:
        session.clear()
        flash("Session expired. Please login again.", "warning")
        return redirect(url_for('auth.login'))

    return render_template('profile.html', user=user)

@user_bp.route('/edit', methods=['GET', 'POST'])
def edit_profile():
    if 'user_id' not in session:
        return redirect(url_for('auth.login'))

    user_repo = RepositoryFactory.get_repository("user")
    user = user_repo.get_by_id(session['user_id'])
    
    # حماية برضه هنا
    if user is None:
        session.clear()
        return redirect(url_for('auth.login'))

    if request.method == 'POST':
        phone = request.form.get('phone')
        address = request.form.get('address')
        shipping_company = request.form.get('shipping_company')
        industry_type = request.form.get('industry_type')
        profile_image = request.form.get('profile_image')

        user_repo.update_user(user.id, phone, address, shipping_company, industry_type, profile_image)
        flash("Profile updated successfully!", "success")
        return redirect(url_for('user.profile'))

    return render_template('edit_profile.html', user=user)

@user_bp.route('/my_shop')
def my_shop():
    if 'user_id' not in session or session.get('role') != 'Producer':
        return redirect(url_for('home'))
    
    listing_repo = RepositoryFactory.get_repository("listing")
    all_listings = listing_repo.get_all_listings()
    my_listings = [l for l in all_listings if l.producer_id == session['user_id']]
    
    return render_template('my_shop.html', listings=my_listings)