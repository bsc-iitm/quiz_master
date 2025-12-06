from flask import Blueprint, render_template, request, jsonify, session
from werkzeug.security import check_password_hash
from models.user import User
from flask_session import Session
import sys
from utils.decorators import login_required, admin_required

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/', methods=['GET'])
def index():
    return render_template('root/login.html')

# from utils.decorators import login_required, admin_required and check user on login
@login_required
@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    if not data:
        return jsonify({'error': 'No JSON received', 'message': 'No JSON data was provided in the request'}), 400

    email = data.get('email')
    password = data.get('password')
    select_user = User.query.filter_by(username=email).first()
    if not select_user:
        return jsonify({
            'error': 'User not found',
            'message': 'No user found with the provided email',
            'success': False
        }), 404
    if not select_user.check_password(password):
        return jsonify({
            'error': 'Invalid password',
            'message': 'The provided password is incorrect',
            'success': False
        }), 401
    # if admis then return to admin dashboard else return to user dashboard and template name 
    if select_user.role == 'admin':
        session['user_id'] = select_user.id
        session['role'] = select_user.role
        return jsonify({
            'message': 'Admin login successful',
            'redirect_url': '/dashboard',
            'user': select_user.to_dict(),
            'success': True
        }), 200
    else:
        session['user_id'] = select_user.id
        session['role'] = select_user.role
        return jsonify({
            'message': 'User login successful',
            'redirect_url': '/dashboard',
            'user': select_user.to_dict(),
            'success': True
        }), 200
@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('root/user_registration.html')

@auth_bp.route('/dashboard', methods=['GET'])
def admin_dashboard():
    if session.get('role') == 'admin':
        return render_template('admin/admin_dashboard.html')
    elif session.get('role') == 'user':
        return render_template('user/user_dashboard.html')
    else:
        return render_template('root/login.html')

