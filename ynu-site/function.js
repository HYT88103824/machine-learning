const bar = document.getElementById('bars');
const menu = document.getElementById('menu');

document.addEventListener("DOMContentLoaded", function () {
    const bgElement = document.querySelector(".bg");
    
    // 背景画像のリスト
    const images = [
      "ynu-photo1.jpg",
      "ynu-photo2.jpg",
      "ynu-photo3.jpg",
      "ynu-photo4.jpg",
      "ynu-photo5.jpg"
    ];
    
    let currentIndex = 0;
  
    // 初期画像をセット
    bgElement.style.backgroundImage = `url(${images[0]})`;
 
  
    function changeBackground() {
      // フェードアウト
      bgElement.style.opacity = 0;
      
      setTimeout(() => {
        // 次の画像へ
        currentIndex = (currentIndex + 1) % images.length; //剰余にすることで反復（0に戻る）
        bgElement.style.backgroundImage = `url(${images[currentIndex]})`;
        
        // フェードイン
        bgElement.style.opacity = 1;
      }, 1500);  // opacityのtransition時間に合わせる
    }
  
    // 5秒ごとに画像を変更
    setInterval(changeBackground, 5000);
  });

bar.addEventListener('click', function(){
    bar.classList.toggle('active');
    menu.classList.toggle('active');
});

// メニュー外をクリックしたら閉じる処理を追加
document.addEventListener("click", function (event) {
    if (!menu.contains(event.target) && !bars.contains(event.target)) {
        menu.classList.remove("active");
}});

//授業の選択=>学部の表示=>学科の表示
document.addEventListener("DOMContentLoaded", function () {
    const lecture = document.getElementById('lecture');
    const faculty = document.getElementById('faculty');
    const major = document.getElementById('major');
    const facultycheck = faculty.querySelectorAll('input[type="checkbox"]');
    const majorcheck = major.querySelectorAll('input[type="checkbox"]');
  
    // 初期状態では非表示にする
    faculty.style.display = 'none';
    major.style.display = 'none';
  
    lecture.addEventListener('change', function() {
//lecture内に学科選択を組み込み, 再度押したときに正常に動くようにする
      if (this.checked) {
        faculty.style.display = 'block';
        major.style.display = 'block';
  
        facultycheck.forEach(function(checkbox) {
          // 学部選択のidと一致する学科の詳細ブロックを取得
          const targetId = checkbox.dataset.target;
          const detail = major.querySelector('div#' + targetId);
  
          if (detail) {
            // 初期設定では詳細ブロックは非表示
            detail.style.display = 'none';
  
            // 学部のチェックボックスが変更されたときの処理
            checkbox.addEventListener('change', function() {
              if (this.checked) {
                detail.style.display = 'block';
              } else {
                // チェックが外れたときは詳細ブロックを非表示にし、中のチェックもリセット
                detail.style.display = 'none';
                const detailInputs = detail.querySelectorAll('input[type="checkbox"]');
                detailInputs.forEach(cb => {
                  cb.checked = false;
                });
              }
            });
          }
        });

      } else {
        faculty.style.display = 'none';
        major.style.display = 'none';
  
        // 学部・学科両方のチェックをリセット
        facultycheck.forEach(function(checkbox) {
          checkbox.checked = false;
        });
        majorcheck.forEach(function(checkbox) {
          checkbox.checked = false;
        });
      }
    });
  });


