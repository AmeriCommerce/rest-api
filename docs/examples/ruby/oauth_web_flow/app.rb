require 'sinatra'
require 'erb'
require './americommerce'

class OAuthWebFlowDemo < Sinatra::Base
	use Rack::Logger

	enable :sessions
	set :api, AmeriCommerce::ApiClient.new

	helpers do
		def logger
			request.logger
		end
	end

	get '/' do
		unless session[:api_user]
			r = CGI::escape(request.base_url)
			return_url = url("/callback?r=#{r}")
			redirect settings.api.start_negotiation_url(return_url)
		end

		token = session[:api_user]
		page = !params[:page].nil? ? params[:page].to_i : 1
		product_list = settings.api.get_product_list(token, page)

		erb :index, :locals => {
			:product_list => product_list,
			:next_button_class => !product_list['next_page'].nil? ? 'next' : 'next disabled',
			:previous_button_class => !product_list['previous_page'].nil? ? 'previous' : 'previous disabled',
			:current_page => !params[:page].nil? ? params[:page].to_i : 1
		}
	end

	get '/callback' do
		r = CGI::escape(params[:r])
		return_url = url("/callback?r=#{r}")

		token_data = settings.api.verify(return_url, params[:auth_id], params[:code])
		token = AmeriCommerce::Token.new(token_data)
		session[:api_user] = token

		redirect params[:r]
	end
end