;; init.el --- Emacs configuration

;; INSTALL PACKAGES
;; --------------------------------------

(require 'package)

(add-to-list 'package-archives
       '("melpa" . "http://elpa.emacs-china.org/melpa/") t)

(package-initialize)
(when (not package-archive-contents)
  (package-refresh-contents))

(defvar kidney_package
  '(better-defaults
    elpy
    material-theme))

(mapc #'(lambda (package)
    (unless (package-installed-p package)
      (package-install package)))
      kidney_package)

;; BASIC CUSTOMIZATION
;; --------------------------------------

;; (setq inhibit-startup-message t) ;; hide the startup message
(load-theme 'material t) ;; load material theme
(global-linum-mode t) ;; enable line numbers globally
(elpy-enable)
(elpy-use-ipython)

;; SHELL
;; ---------------------------------------
(autoload 'ansi-color-for-comint-mode-on "ansi-color" nil t)
(add-hook 'shell-mode-hook 'ansi-color-for-comint-mode-on t)

;; init.el ends here

