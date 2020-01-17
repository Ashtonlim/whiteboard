const path = require('path');
const MiniCssExtractPlugin = require('mini-css-extract-plugin');

module.exports = {
    entry: './vidboard/src/js/index.js',
    plugins: [
        new MiniCssExtractPlugin({filename: '[name].css'}),
    ],
    module: {
        rules: [
            {
                test: /\.scss$/,
                use: [
                    {
                        loader: MiniCssExtractPlugin.loader,
                        options: {
                            // you can specify a publicPath here
                            // by default it uses publicPath in webpackOptions.output
                            // publicPath: '/css',
                            hmr: true,
                        },
                    },
                    'css-loader',
                    'sass-loader'
                ]
            },
            {
                test:/\.({svg|png|jgp|gif})$/,
                use: {
                    loader: 'file-loader',
                    options: {
                        name: '[name].[ext]'
                    }
                }
            }
            
        ]
    }
};