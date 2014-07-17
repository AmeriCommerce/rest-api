require 'yaml'
require 'json'
require 'digest'
require 'net/http'
require 'uri'
require 'openssl'

module AmeriCommerce

	class ApiClient
		def initialize
			config = YAML.load_file('config.yml')

			@app_id = config['app_id']
			@app_secret = config['app_secret']
			@app_scope = config['app_scope']
			@store_domain = config['store_domain']
		end

		def start_negotiation_url(return_url)
			"https://#{@store_domain}/api/oauth?client_id=#{@app_id}&scope=#{@app_scope}&redirect_uri=#{return_url}"
		end

		def verify(return_url, auth_id, code)
			sig = create_signature(@app_secret, code, @app_id, @app_scope, return_url.downcase)
			data = {
				:client_id => @app_id,
				:auth_id => auth_id,
				:signature => sig
			}.to_json
			headers = {
				'Content-Type' => 'application/json'
			}

			uri = URI("https://#{@store_domain}/api/oauth/access_token")
			http = Net::HTTP.new(uri.host, uri.port)
			http.use_ssl = true
			# if using a development cert
			# http.verify_mode = OpenSSL::SSL::VERIFY_NONE

			response = http.post(uri.path, data, headers)
			JSON.parse(response.body)
		end

		def get_product_list(token, page)
			headers = {
				'X-AC-Auth-Token' => token.access_token
			}

			uri = URI("https://#{@store_domain}/api/v1/products")
			http = Net::HTTP.new(uri.host, uri.port)
			http.use_ssl = true
			# if using a development cert
			# http.verify_mode = OpenSSL::SSL::VERIFY_NONE

			response = http.get(uri.path + "?page=#{page}", headers)
			JSON.parse(response.body)
		end

	private

		def create_signature(*args)
			combined = args.join('')
			sha256 = Digest::SHA256.new
			sha256.update(combined).to_s
		end
	end

	class Token
		attr_reader :access_token, :refresh_token, :expires

		def initialize(data)
			@access_token = data['access_token']
			@refresh_token = data['refresh_token']
			@expires = data['expires']
		end
	end

end