layout_name=colors

# copy files
current_dir=$(pwd)
cd $QMK_HOME || exit 1
mkdir keyboards/zsa/moonlander/keymaps/$layout_name
cp $current_dir/*.c keyboards/zsa/moonlander/keymaps/$layout_name/
cp $current_dir/*.h keyboards/zsa/moonlander/keymaps/$layout_name/
cp $current_dir/rules.mk keyboards/zsa/moonlander/keymaps/$layout_name/
# compile layout
qmk compile -kb zsa/moonlander -km $layout_name
