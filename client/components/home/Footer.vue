<template>
    <footer class="relative bg-gradient-to-t dark:from-gray-950 from-gray-200 to-gray-100 dark:to-gray-900 pt-24">
        <div class="absolute inset-0 overflow-hidden">
            <div class="absolute bottom-0 left-1/2 -translate-x-1/2 w-[800px] h-[500px] bg-gradient-to-t from-sky-500/10 to-transparent rounded-full blur-3xl"></div>
        </div>
        
        <div class="relative max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="grid grid-cols-1 md:grid-cols-3 gap-12 pb-12">
                <div class="space-y-4">
                    <div class="flex items-center space-x-4">
                        <div class="bg-gradient-to-tr from-sky-400 to-blue-600 p-2.5 rounded-xl shadow-lg shadow-sky-500/20">
                            <Icon name="svg-spinners:wind-toy" class="w-6 h-6 text-white" />
                        </div>
                        <span class="text-xl font-bold bg-gradient-to-r from-sky-400 to-blue-600 bg-clip-text text-transparent">Vaidya</span>
                    </div>
                    <p class="text-gray-400">
                        Providing cutting-edge weather analytics for sustainable agriculture and renewable energy.
                    </p>
                </div>
                
                <div class="space-y-4">
                    <h4 class="text-lg font-semibold bg-gradient-to-r from-sky-400 to-blue-600 bg-clip-text text-transparent">Quick Links</h4>
                    <ul class="space-y-3">
                        <li>
                            <a href="#" class="text-gray-400 hover:text-sky-400 transition-colors duration-300">Services</a>
                        </li>
                        <li>
                            <a href="#" class="text-gray-400 hover:text-sky-400 transition-colors duration-300">About</a>
                        </li>
                        <li>
                            <a href="#" class="text-gray-400 hover:text-sky-400 transition-colors duration-300">Contact</a>
                        </li>
                    </ul>
                </div>
                
                <div class="space-y-4">
                    <h4 class="text-lg font-semibold bg-gradient-to-r from-blue-600 to-indigo-600 bg-clip-text text-transparent">Contact</h4>
                    <ul class="space-y-2">
                        <li class="text-gray-600 dark:text-gray-300">Email: contact@vaidya.com</li>
                        <li class="text-gray-600 dark:text-gray-300">Phone: (555) 123-4567</li>
                    </ul>
                </div>
            </div>
            
            <div class="border-t border-gray-200 dark:border-gray-700/50 py-8">
                <p class="text-center text-gray-500 dark:text-gray-400">
                    © {{ new Date().getFullYear() }} Vaidya Insights. All rights reserved.
                </p>
            </div>
        </div>
    </footer>
</template>