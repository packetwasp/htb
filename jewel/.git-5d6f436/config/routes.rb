Rails.application.routes.draw do
  get 'home/index'
  get 'articles/index'
  get 'signup', to: 'users#new'
  get 'login', to: 'sessions#new'
  post 'login', to: 'sessions#create'
  delete 'logout', to: 'sessions#destroy'

  resources :articles
  resources :users, except: [:new]

  root 'home#index'
end
