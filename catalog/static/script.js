var selectedCategory = null;

  // Обработчик события изменения состояния чекбоксов
  document.addEventListener('change', function(event) {
    if (event.target.classList.contains('check')) {
      var newSelectedCategory = event.target.value;

      if (selectedCategory === null) {
        selectedCategory = newSelectedCategory;
      } else {
        if (newSelectedCategory === selectedCategory) {
          console.log('Выбранная категория не содержится в категории товара');
        } else {
          console.log('Выбранная категория содержится в категории товара');
          
        }
        selectedCategory = null;
      }
    }
  });