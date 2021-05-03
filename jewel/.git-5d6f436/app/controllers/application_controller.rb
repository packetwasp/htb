class ApplicationController < ActionController::Base
  protect_from_forgery with: :exception
  helper_method :current_user, :logged_in?, :current_username, :current_userid, :can_write?

  def current_user
    @current_user ||= User.find(session[:user_id]) if session[:user_id] and User.exists?(session[:user_id])
  end

  def logged_in?
    !!current_user
  end

  def can_write?
    if logged_in?
      @current_user = current_user
      return @current_user.can_write 
    else
      return false
    end
  end

  def require_user
    if !logged_in?
      flash[:danger] = "You must be logged in to perform this action"
      redirect_to login_path
    end
  end

  def current_username
    if session[:user_id]
      cache = ActiveSupport::Cache::RedisCacheStore.new(url: "redis://127.0.0.1:6379/0")
      @current_username = cache.fetch("username_#{session[:user_id]}", raw: true) do
        @current_user = current_user
        @current_username = @current_user.username
      end
    else
      @current_username = "guest"
    end
    return @current_username
  end

  def current_userid
    return session[:user_id] if session[:user_id]
  end
end
