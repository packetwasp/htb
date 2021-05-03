class ArticlesController < ApplicationController
  before_action :require_user, only: [:new, :create, :update, :destroy]

  def index
    @articles = Article.paginate(page: params[:page], per_page: 3)
  end

  def show
    @article = Article.find(params[:id])
  end

  def new
    @article = Article.new
  end

  def edit
    @article = Article.find(params[:id])
  end

  def create
    @curr_user = current_user
    if @curr_user.can_write
      @article = Article.new(article_params)
      #@article.user = User.first
      @article.user = @curr_user
      if @article.save
        flash[:success] = "Article was successfully created"
        redirect_to @article
      else
        render 'new'
      end
    else
      flash[:danger] = "You are not allowed to post articles"
      redirect_to articles_path
    end
  end

  def update
    @article = Article.find(params[:id])
 
    if @article.update(article_params)
      flash[:success] = "Article was updated"
      redirect_to @article
    else
      flash[:success] = "Article was not updated"
      render 'edit'
    end
  end

  def destroy
    @article = Article.find(params[:id])
    if @article.user && @article.user == current_user
      @article.destroy
      flash[:success] = "Article was deleted"
      redirect_to articles_path
    else
      flash[:danger] = "Not authorized"
      redirect_to articles_path
    end
  end

  private
    def article_params
      params.require(:article).permit(:title, :text)
    end
end
