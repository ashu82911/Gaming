package com.playandwin

import android.annotation.SuppressLint
import android.os.Bundle
import android.webkit.WebChromeClient
import android.webkit.WebSettings
import android.webkit.WebView
import android.webkit.WebViewClient
import android.view.View
import android.widget.ProgressBar
import androidx.appcompat.app.AppCompatActivity

class MainActivity : AppCompatActivity() {

    private lateinit var webView: WebView
    private lateinit var progressBar: ProgressBar

    // 🔁 Replace with your Streamlit URL after deployment
    private val APP_URL = "https://playandwin-ashu.streamlit.app"

    @SuppressLint("SetJavaScriptEnabled")
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        webView     = findViewById(R.id.webView)
        progressBar = findViewById(R.id.progressBar)

        // WebView settings
        webView.settings.apply {
            javaScriptEnabled       = true
            domStorageEnabled       = true
            loadWithOverviewMode    = true
            useWideViewPort         = true
            setSupportZoom(true)
            builtInZoomControls     = true
            displayZoomControls     = false
            cacheMode               = WebSettings.LOAD_DEFAULT
            mixedContentMode        = WebSettings.MIXED_CONTENT_ALWAYS_ALLOW
            mediaPlaybackRequiresUserGesture = false
        }

        webView.webViewClient = object : WebViewClient() {
            override fun onPageFinished(view: WebView?, url: String?) {
                progressBar.visibility = View.GONE
            }
        }

        webView.webChromeClient = object : WebChromeClient() {
            override fun onProgressChanged(view: WebView?, newProgress: Int) {
                progressBar.progress = newProgress
                progressBar.visibility = if (newProgress < 100) View.VISIBLE else View.GONE
            }
        }

        webView.loadUrl(APP_URL)
    }

    // Handle back button
    override fun onBackPressed() {
        if (webView.canGoBack()) webView.goBack()
        else super.onBackPressed()
    }
}
