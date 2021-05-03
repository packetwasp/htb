class UsersController < ApplicationController
  before_action :require_user, only: [:update]

#  def index
#    @users = User.paginate(page: params[:page], per_page: 3)
#  end

  def show
    @user = User.find(params[:id])
    @current_user = current_user
    @user_articles = @user.articles.paginate(page: params[:page], per_page: 333333333)
  end

  def new
    @user = User.new
  end

  def edit
    @user = User.find(params[:id])
  end

  def create
    @user = User.new(user_params)
    if @user.save
      flash[:success] = "User successfully registered: #{@user.username}"
      redirect_to articles_path
    else
      render 'new'
    end
  end

  def update
    @user = User.find(params[:id])
    if @user && @user == current_user
      cache = ActiveSupport::Cache::RedisCacheStore.new(url: "redis://127.0.0.1:6379/0")
      cache.delete("username_#{session[:user_id]}")
      @current_username = cache.fetch("username_#{session[:user_id]}", raw: true) {user_params[:username]}
      if @user.update(user_params)
        flash[:success] = "Your account was updated successfully"
        redirect_to articles_path
      else
        cache.delete("username_#{session[:user_id]}")
        render 'edit'
      end
    else
      flash[:danger] = "Not authorized"
      redirect_to articles_path
    end
  end

  private
    def user_params
    params.require(:user).permit(:username, :email, :password)
  end
end
